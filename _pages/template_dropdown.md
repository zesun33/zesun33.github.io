---
layout: page
title: submenus
nav: false  # Set to true when you want to enable dropdown
nav_order: 8
dropdown: true
published: false
category: hidden
children:
  - title: First Submenu Item
    permalink: /submenu1/
  - title: divider  # Creates a visual separator
  - title: Second Submenu Item
    permalink: /submenu2/
  - title: Third Submenu Item
    permalink: /submenu3/
---

# Template Dropdown Menu

This page creates a dropdown navigation menu. The `children` list above defines the dropdown items.

### How to Use:
1. Update the `children` list with your actual submenu items
2. Create the corresponding pages for each permalink
3. Use `divider` to add visual separators
4. Set `nav: true` and `published: true` when ready to display

### Example Children Options:
```yaml
children:
  - title: Research Areas
    permalink: /research/
  - title: divider
  - title: Lab Resources
    permalink: /resources/
  - title: Collaborations
    permalink: /collaborations/
``` 