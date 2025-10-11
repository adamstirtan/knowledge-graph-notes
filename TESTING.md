# Testing Guide

This document describes how to test the knowledge graph website.

## Manual Testing Checklist

### Initial Load
- [ ] Page loads without errors
- [ ] Dark background (#1a1a1a) is applied
- [ ] Header is visible in top-left with name "Adam Stirtan"
- [ ] Social links (GitHub, LinkedIn, Contact) are visible and clickable
- [ ] Graph canvas fills the entire viewport
- [ ] Loading message appears initially

### Graph Visualization
- [ ] All nodes render as rectangles
- [ ] Nodes are connected by lines (edges)
- [ ] Nodes have labels showing post titles
- [ ] Force simulation creates a natural layout
- [ ] Graph focuses on the most recent post (top node) after 1 second
- [ ] Nodes that share tags are connected

### Interaction
- [ ] **Pan**: Click and drag the background to pan the view
- [ ] **Zoom**: Scroll wheel or pinch to zoom in/out
- [ ] **Drag Node**: Click and drag a node to move it
- [ ] **Click Node**: Click a node to open the post overlay
- [ ] **Close Overlay**: Click X button, click outside card, or press ESC

### Post Overlay
- [ ] Overlay appears with smooth animation
- [ ] Post date is displayed at the top
- [ ] Markdown content is properly rendered
- [ ] Code blocks have syntax highlighting background
- [ ] Links open in new tab (external)
- [ ] Images are displayed (if present in post)
- [ ] Scrollbar appears if content is long
- [ ] Close button (X) is visible in top-right

### Responsive Behavior
- [ ] Window resize updates graph layout
- [ ] Canvas resizes to fill viewport
- [ ] Header remains fixed on scroll/zoom
- [ ] Overlay is centered on different screen sizes

### Data Loading
- [ ] Posts are loaded from posts.json
- [ ] All 6 example posts are visible
- [ ] If posts.json fails, sample posts are used as fallback
- [ ] Post connections reflect shared tags:
  - post1 & post2: share "javascript"
  - post1 & post3: share "web"
  - post2 & post4: share "visualization"
  - post2 & post5: share "javascript"
  - post4 & post6: share "visualization"
  - etc.

## Automated Validation

Run the validation script to check all post JSON files:

```bash
python3 validate_posts.py
```

This script validates:
- All required fields are present (timestamp, text, tags)
- Field types are correct (tags must be array)
- At least one tag is present
- JSON syntax is valid

## Browser Compatibility

Test in the following browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Testing

- [ ] Graph renders smoothly with 6 nodes
- [ ] Pan and zoom are responsive
- [ ] Overlay opens/closes without lag
- [ ] Window resize doesn't cause stuttering

## Deployment Testing

After deploying to production:
1. Verify D3.js and Marked.js load from CDN
2. Confirm all images load correctly
3. Test all social links open correct pages
4. Verify email link opens mail client

## Known Limitations

### CDN Dependencies
- **D3.js** (v7) and **Marked.js** are loaded from CDN
- If CDNs are blocked or unavailable:
  - The loading screen will show an error message
  - The graph will not render
  - **Mitigation**: Download libraries locally and update script tags in index.html
  - **Alternative**: The page includes fallback sample posts if posts.json fails to load

### Protocol Limitations
- Local `file://` protocol may have CORS issues for JSON loading
- **Solution**: Use a local web server (see README for instructions)

### Display Considerations
- Best viewed on desktop browsers (mobile works but has smaller nodes)
- Requires modern browser with ES6+ JavaScript support

## Adding Test Posts

To test adding new posts:

1. Create a new JSON file: `posts/test-post.json`
```json
{
    "timestamp": "2025-01-20T12:00:00Z",
    "text": "# Test Post\n\nThis is a test.",
    "tags": ["test"]
}
```

2. Add to `posts.json`: `"test-post.json"`
3. Refresh page
4. Verify new node appears
5. Verify it connects to nodes with shared tags
