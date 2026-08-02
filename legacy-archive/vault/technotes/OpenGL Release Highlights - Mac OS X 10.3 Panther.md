---
title: OpenGL Release Highlights - Mac OS X 10.3 Panther
apple_id: DTS10003485
resource_type: Technical Note
platform: macOS
topic: null
technology: null
published: '2005-02-04'
source_url: https://developer.apple.com/library/archive/technotes/tn2131/_index.html
archived_at: '2026-07-26T19:53:51.039229Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2131

# OpenGL Release Highlights - Mac OS X 10.3 Panther

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

OpenGL Release Highlights - Mac OS X 10.3 Panther

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4mi)[10.3.0](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4mq)[10.3.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4my)[10.3.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4na)[10.3.3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4ni)[10.3.4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4nq)[10.3.5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4ny)[10.3.6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4oa)[10.3.7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwugsbrfvjukq2ujfhu4oi)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbyguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

This document describes the features and fixes made to OpenGL in the indicated version of Mac OS X. Included with the list of Radar numbers is a short description that offers some insight as to the nature of the problem. This list is not meant to be an all-encompassing list of things fixed but rather the highlights of the code changes that would be relevant to the developer community.

[Back to Top](#)

## 10.3.0

__3117825 :__

__Resolution :__  This was a driver-level problem where textures were being deallocated improperly.

__3214539 :__

__Resolution :__  Fixed

__3248168 :__

__Resolution :__  Fixed

__3273703 :__

__Resolution :__  Subwindows are synchronized between GLUT and AppKit now.

__3332101 :__

__Resolution :__  This was a problem with how GLUT was processing work events.

__3332139 :__

__Resolution :__  This problem was caused by the GLUT reshape event not being called under certain circumstances.

__3357397 :__

__Resolution :__  This was the result of some problems with the vertex program emulation code on certain hardware.

__3385643 :__

__Resolution :__  Fixed

__3392756 :__

__Resolution :__  Fixed

[Back to Top](#)

## 10.3.1

No significant changes.

[Back to Top](#)

## 10.3.2

No significant changes.

[Back to Top](#)

## 10.3.3

No significant changes.

[Back to Top](#)

## 10.3.4

No significant changes.

[Back to Top](#)

## 10.3.5

__3581588 :__

__Resolution :__ Vertex program geometry corruption problem has been fixed.

__3591587 :__

__Resolution :__ This bug is the result of a memory management related crash in the ATI Rage128 driver.

[Back to Top](#)

## 10.3.6

__3602308 :__

__Resolution :__  Renderer ID was not being reported correctly for Rage 128 cards.

__3642383 :__

__Resolution :__ Change in behavior of how display lists function - creation of display lists is slow but usage is faster.

__3783539 :__

__Resolution :__ Performance enhancement for display lists that uses vertex arrays for storing display list data

__3798721 :__

__Resolution :__ Problem with the retrieval of generic compressed types

__3798729 :__

__Resolution :__ The logic for performing the floating point value clamping was not working properly.

__3805479 :__

__Resolution :__ Returns correct renderer ID for this application.

__3809966 :__

__Resolution :__ Erroneous code path was being taken by vertex and fragment program emulator.

[Back to Top](#)

## 10.3.7

__3864234 :__

__Resolution :__ Leaking a vertex array object of about 4k with small display lists.

__3868287 :__

__Resolution :__ An object was not being freed upon deletion of the CGLContext.

__3873404 :__

__Resolution :__ Problem with the logic that evaluated luminance alpha sources

__3889158 :__

__Resolution :__ Problem with fragment and vertex program processing to generate an inverse model view matrix.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-02-04 | Changed title from "OpenGL Release Notes" to "OpenGL Release Highlights". |
| 2005-01-26 | New document that contains a list of bugs along with a short description on a release-by-release basis |

