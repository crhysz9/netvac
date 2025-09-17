# Netvac API Documentation

## Introduction

This document outlines the API for Netvac, a network vacuum cleaner.  It details the available endpoints, request parameters, and response formats.

## Authentication

All API requests require an API key.  Include your key in the `X-API-Key` header of your requests.  You can obtain an API key by contacting support.

## Endpoints

### `/scan`

**Method:** `POST`

**Description:** Initiates a network scan.

**Request Parameters:**

* `target`: (string, required) The IP address or network range to scan.  e.g., `192.168.1.1` or `192.168.1.0/24`
* `ports`: (array of integers, optional)  A list of ports to scan. Defaults to a common set of ports.

**Response:**

* `status`: (string) `success` or `error`
* `scan_id`: (integer)  A unique identifier for the scan.  Use this ID to retrieve scan results.
* `message`: (string)  A message indicating success or the reason for failure.


### `/results/{scan_id}`

**Method:** `GET`

**Description:** Retrieves the results of a scan.

**Parameters:**

* `scan_id`: (integer, required) The ID of the scan.

**Response:**

* `status`: (string) `success` or `error`
* `scan_id`: (integer) The ID of the scan.
* `results`: (array of objects) An array of objects, each representing a host found during the scan.  Each object contains the following:
    * `ip`: (string) The IP address of the host.
    * `open_ports`: (array of integers) A list of open ports on the host.
    * `os`: (string) The operating system detected on the host (if detected).
* `message`: (string)  A message indicating success or the reason for failure.


### `/cleanup/{ip}`

**Method:** `POST`

**Description:** Attempts to mitigate vulnerabilities on a specific host.  This might involve blocking malicious activity or patching security flaws.


**Parameters:**

* `ip`: (string, required) The IP address of the host.

**Response:**

* `status`: (string) `success` or `error`
* `ip`: (string) The IP address of the cleaned host.
* `message`: (string)  A message indicating success or the reason for failure.



## Error Codes

* `400`: Bad Request - Invalid request parameters.
* `401`: Unauthorized - Missing or invalid API key.
* `404`: Not Found - Scan not found or host not found.
* `500`: Internal Server Error - An unexpected error occurred on the server.


## Rate Limiting

The API has a rate limit to prevent abuse.  If you exceed the rate limit, you will receive a `429` Too Many Requests error.


## Example using cURL

```bash
curl -X POST \
  https://api.netvac.com/scan \
  -H 'X-API-Key: YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "target": "192.168.1.0/24",
    "ports": [22, 80, 443]
  }'
```

 -->