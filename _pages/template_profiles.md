---
layout: profiles
permalink: /people/
title: people
description: members of the lab or group
nav: false  # Set to true when you want to enable
nav_order: 7
published: false
category: hidden

profiles:
  # Template for lab members or group members
  # Duplicate this block for each member
  - align: right
    image: member1_pic.jpg
    content: about_member1.md
    image_circular: false # crops the image to make it circular
    more_info: >
      <p>Office: Room 123</p>
      <p>Email: member@university.edu</p>
      <p>Research Area: Your research focus</p>
  - align: left
    image: member2_pic.jpg
    content: about_member2.md
    image_circular: false # crops the image to make it circular
    more_info: >
      <p>Office: Room 456</p>
      <p>Email: member2@university.edu</p>
      <p>Research Area: Another research focus</p>
---

This page showcases lab members, research group participants, or collaborators.

### How to Use:
1. Add profile images to `assets/img/`
2. Create content files in `_pages/` for each member
3. Update the profiles section above
4. Set `nav: true` and `published: true` when ready to display 