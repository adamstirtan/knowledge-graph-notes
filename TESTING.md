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

Run the validation script to check all features:

```bash
python3 << 'EOF'
import json

# Validate JSON files
for i in range(1, 7):
    with open(f'posts/post{i}.json') as f:
        post = json.load(f)
        assert 'timestamp' in post, f"post{i} missing timestamp"
        assert 'text' in post, f"post{i} missing text"
        assert 'tags' in post, f"post{i} missing tags"
        assert isinstance(post['tags'], list), f"post{i} tags not an array"
        assert len(post['tags']) > 0, f"post{i} has no tags"
        print(f"✓ post{i}.json valid")

print("\nAll JSON files validated successfully!")
EOF
```

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

- CDN resources (D3.js, Marked.js) must be accessible
- Local file:// protocol may have CORS issues for JSON loading
- Best viewed on desktop browsers (mobile works but smaller nodes)

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
