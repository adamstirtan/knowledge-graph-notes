#!/usr/bin/env python3
"""
Validation script for post JSON files.
Run this to ensure all posts have required fields and valid structure.
"""

import json
import sys
from pathlib import Path

def validate_post(filepath):
    """Validate a single post JSON file."""
    try:
        with open(filepath) as f:
            post = json.load(f)
        
        # Check required fields
        required_fields = ['timestamp', 'text', 'tags']
        for field in required_fields:
            if field not in post:
                return False, f"Missing required field: {field}"
        
        # Validate field types
        if not isinstance(post['tags'], list):
            return False, "Field 'tags' must be an array"
        
        if len(post['tags']) == 0:
            return False, "Field 'tags' must have at least one tag"
        
        # Validate optional fields if present
        if 'image' in post and not isinstance(post['image'], str):
            return False, "Field 'image' must be a string"
        
        return True, "Valid"
    
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def main():
    """Validate all post JSON files."""
    posts_dir = Path('posts')
    
    if not posts_dir.exists():
        print("Error: 'posts' directory not found")
        sys.exit(1)
    
    post_files = sorted(posts_dir.glob('*.json'))
    
    if not post_files:
        print("Warning: No JSON files found in 'posts' directory")
        sys.exit(0)
    
    print("Validating post JSON files...")
    print("=" * 60)
    
    all_valid = True
    for filepath in post_files:
        valid, message = validate_post(filepath)
        status = "✓" if valid else "✗"
        print(f"{status} {filepath.name}: {message}")
        if not valid:
            all_valid = False
    
    print("=" * 60)
    if all_valid:
        print(f"✅ All {len(post_files)} post files validated successfully!")
        sys.exit(0)
    else:
        print("❌ Some post files have validation errors")
        sys.exit(1)

if __name__ == '__main__':
    main()
