terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
  }
}

provider "azurerm" {
}

resource "azurerm_resource_group" "adi_resource_group" {
  name     = "Tf_test_project"
  location = "West US 2"
}

resource "azurerm_storage_account" "adi_storage_acc" {
  name                     = "aditftesting"
  resource_group_name      = azurerm_resource_group.adi_resource_group.name
  location                 = azurerm_resource_group.adi_resource_group.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "adi_container" {
  name                  = "testcontent"
  storage_account_name  = azurerm_storage_account.adi_storage_acc.name
}
