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

Posts are stored in the file `posts.json` as follows:

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

### Navigation

- **Pan**: Click and drag on the canvas background
- **Zoom**: Use mouse wheel or pinch gesture
- **View Post**: Click on any node to open the post overlay
- **Close Post**: Click the X button, click outside the card, or press ESC

## Technology

- **D3.js**: Force-directed graph layout and visualization
- **Marked.js**: Markdown rendering
- **Vanilla JavaScript**: No framework dependencies
- **CSS3**: Modern styling with animations
