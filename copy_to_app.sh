#!/bin/bash

SOURCE_DIR="/Users/mincom/Developer/odoo-17.0/addons/base_document"
DEST_DIR="/Users/mincom/IdeaProjects/DynamicTariffApp/backend/odoo_addon/base_document"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Copy contents from the source to the destination directory
cp -R "$SOURCE_DIR/"* "$DEST_DIR/"

# Optional: Print a message indicating the operation is complete
echo "Contents of $SOURCE_DIR have been copied to $DEST_DIR"
