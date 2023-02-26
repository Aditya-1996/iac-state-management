terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.0.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}

  client_id       = "${var.client_id}"
  client_secret   = "${var.client_secret}"
  tenant_id       =  "${var.tenant_id}"
  subscription_id = "${var.subscription_id}"
}

resource "azurerm_resource_group" "new_tf_rg" {
  name     = "terraform_resources_group"
  location = "West US 2"
}


# resource "azurerm_storage_account" "tftesting" {
#   name                     = "terraformtestsa"
#   resource_group_name      = azurerm_resource_group.new_tf_rg.name
#   location                 = azurerm_resource_group.new_tf_rg.location
#   account_tier             = "Standard"
#   account_replication_type = "LRS"
# }

resource "azurerm_storage_account" "tftesting" {
  name                     = "terraformtestadi96"
  resource_group_name      = azurerm_resource_group.new_tf_rg.name
  location                 = azurerm_resource_group.new_tf_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}


resource "azurerm_storage_container" "simpleblobtest" {
  name                  = "aditestcontents"
  storage_account_name  = azurerm_storage_account.tftesting.name
  container_access_type = "blob"
}

resource "azurerm_storage_blob" "example" {
  name                   = "Adi_resume.pdf"
  storage_account_name   = azurerm_storage_account.tftesting.name
  storage_container_name = azurerm_storage_container.simpleblobtest.name
  type                   = "Block"
  source                 = "Adi_resume.pdf"
}