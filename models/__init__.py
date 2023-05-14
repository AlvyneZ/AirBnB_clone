#!/usr/bin/python3
"""
Initializer for the base_model module
Starts up the storage
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
