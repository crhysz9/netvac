from netvac.backend.models.inventory import Inventory

class InventoryService:
    def add_item(self, item_id, item_name, quantity, unit_price):
        inventory_item = Inventory(item_id, item_name, quantity, unit_price)
        inventory_item.add_item()

    def update_item(self, item_id, new_quantity, new_unit_price):
        inventory_item = Inventory.get_item(item_id)
        if inventory_item:
            inventory_item.update_item(new_quantity, new_unit_price)
        else:
            print("Item not found.")

    def delete_item(self, item_id):
        inventory_item = Inventory.get_item(item_id)
        if inventory_item:
            inventory_item.delete_item()
        else:
            print("Item not found.")

    def get_item(self, item_id):
        return Inventory.get_item(item_id)