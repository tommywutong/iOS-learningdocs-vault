---
title: PassKit Package Format Reference
apple_id: TP40012026
resource_type: Guide
platform: watchOS|iOS
topic: User Experience
technology: PassKit
published: '2017-11-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/Introduction.html
archived_at: '2026-07-27T06:57:08.728144Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Package%20Structure.md)

# About Pass Files

__Companion Guide:__ _[Wallet Developer Guide](../Wallet%20Developer%20Guide/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojv)_

Passes are a digital representation of information that might otherwise be printed on small pieces of paper or plastic. They let users take an action in the physical world, in the same way as boarding passes, membership cards, and coupons.

## At a Glance

This document covers the file format used by the PassKit framework to describe passes.

### Understanding the Package Structure

Pass files are stored on disk as a zipped package containing JSON files and other resources.

__Relevant Chapters:__ [Package Structure](Package%20Structure.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdamrwfvbuqmjnknltc)

### Understanding the Keys

The `pass.json` file contains a dictionary that contains most of the information about the pass.

__Relevant Chapters:__ [Top-Level Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/TopLevel.html#//apple_ref/doc/uid/TP40012026-CH2-SW1), [Lower-Level Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/LowerLevel.html#//apple_ref/doc/uid/TP40012026-CH3-SW1), [Field Dictionary Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/FieldDictionary.html#//apple_ref/doc/uid/TP40012026-CH4-SW1)

[Next](Package%20Structure.md)
