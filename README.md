# Adam's Personal Website

A single-page, dark-mode personal website that represents posts as an interactive knowledge graph.

## Features

- **Interactive Knowledge Graph**: Posts are displayed as nodes in a force-directed graph
- **Tag-Based Connections**: Nodes automatically connect when they share tags
- **Dark Mode**: Minimalist dark theme optimized for readability
- **Markdown Support**: Posts are written in Markdown with full formatting support
- **Smooth Interactions**: Pan, zoom, and click nodes to view post details
- **Responsive**: Works on desktop and mobile devices

## Usage

### Viewing the Website

Simply open `index.html` in a modern web browser. The website works locally without a server, though using a local server is recommended for the best experience:

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js
npx http-server

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

### Adding Posts

Posts are stored as JSON files in the `posts/` directory. Each post file should have:

```json
{
    "timestamp": "2025-01-15T10:00:00Z",
    "text": "# Post Title\n\nPost content in Markdown format...",
    "image": "path/to/image.jpg",
    "tags": ["tag1", "tag2", "tag3"]
}
```

**Required fields:**
- `timestamp`: ISO 8601 date/time string
- `text`: Markdown-formatted content
- `tags`: Array of tag strings (nodes with shared tags will be connected)

**Optional fields:**
- `image`: Path to a local image file (displayed above the post content)

After adding a new post:
1. Create a new JSON file in the `posts/` directory
2. Add the filename to `posts.json`
3. (Optional) Run `python3 validate_posts.py` to validate your post
4. Refresh the page

### Navigation

- **Pan**: Click and drag on the canvas background
- **Zoom**: Use mouse wheel or pinch gesture
- **View Post**: Click on any node to open the post overlay
- **Close Post**: Click the X button, click outside the card, or press ESC

## Deployment

### GitHub Pages

1. Push the repository to GitHub
2. Go to Settings > Pages
3. Set source to main branch
4. Your site will be available at `https://username.github.io/repository-name/`

### Other Hosting

Since this is a static website, you can host it on:
- Netlify
- Vercel
- Any static hosting service
- Any web server

Simply upload all files and ensure `index.html` is in the root directory.

## Technology

- **D3.js**: Force-directed graph layout and visualization
- **Marked.js**: Markdown rendering
- **Vanilla JavaScript**: No framework dependencies
- **CSS3**: Modern styling with animations

## License

MIT License
