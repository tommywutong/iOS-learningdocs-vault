---
title: Automation Release Notes for OS X v10.7
apple_id: TP40001840
resource_type: Release Note
platform: macOS
topic: Interapplication Communication
technology: Automator
published: '2012-03-14'
source_url: https://developer.apple.com/library/archive/releasenotes/AppleApplications/RN-Automator/index.html
archived_at: '2026-07-18T02:50:20.552207Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Automation Release Notes

OS X Lion contains import updates and changes to the automation technologies (AppleScript - Automator - Services - Terminal), as well as numerous enhancements.

#### Contents:

- [Automator/Services](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [AppleScript](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Terminal](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Automator/Services

- New RTF support for most Text actions
- Improved "parsing" of text content for Services
- A number of new actions:

  - Text To ePub
  - Website PopUp
  - Create Banner
  - Get Web Content (Webarchive type)
  - Save Images from Web Content
  - Encode to MPEG Audio
  - Encode Media
  - Add Annotations to Media
- "Convert to …" functionality between Automator document types (File Menu)
- The Plugin Installer to install Actions, Services, and other types of workflows
- Action Developers:

  - Updated action APIs with better error handling
  - Formatters in TokenFields
  - AMCustomInputType for custom service types
  - Webarchive and Rich Text types available
- New Services:

  - Encode Selected Movie Files (Finder)
  - Encode Selected Audio Files (Finder)

### AppleScript

- Support for creating and editing ASOC (AppleScript-Objective C) applets in AppleScript Editor
- You can call C functions from ASOC
- Xcode 4's unified Editor now has support for AppleScript
- AppleScript Editor can be used as an External Editor

### Terminal

Support for appearance:

- Editable ANSI colors in Preferences
- Support for 256 colors
- Default TERM value is now xterm-256color
- BCE (background color erase)
- Background images, including randomized images from folders
- Privacy Glass
- Scrollbars now hidden
- Full screen Terminal
- Better alternate screen support

Status Information in tabs and minimized windows:

- Show live content
- Unread text indicator
- Bell count indicator
- Busy indicator (also in tabs closed box), current process
- Tab title
