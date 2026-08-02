---
title: Unable to select input device in AU Lab
apple_id: DTS10004312
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2007-05-17'
source_url: https://developer.apple.com/library/archive/qa/qa1526/_index.html
archived_at: '2026-07-18T02:32:11.949722Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1526

# Unable to select input device in AU Lab

## Q:  Why am I unable to select an input device in AU Lab

A: Why am I unable to select an input device in AU Lab

AU Lab requires that input and output tracks be created on the same physical device. When running on a computer such as an Intel-based Mac or attempting to use a built-in digital I/O device the solution is to use the Audio MIDI Setup application to create an Aggregate device (under File menu) and then add your required devices to the aggregate, thus appearing as a single physical device to AU Lab.

__How to create an aggregate device__

1. Launch Audio MIDI Setup.app and select 'Open Aggregate Device Editor' from File menu

   <IMAGE>
2. Click the '+' icon to create a new aggregate, a list of real devices should then appear in the 'Structure' box.
3. Enable the 'Use' checkbox for real devices you would like included in the aggregate device

   <IMAGE>
4. The aggregate device should now show (x) inputs and (x) outputs (number of inputs/outputs may vary depending on configuration), click Done.

   ...now launch AU Lab
5. The aggregate should now appear in the 'Audio Device' popup menu, select it.

   <IMAGE>
6. Add any appropriate outputs
7. Click the 'Inputs' tab and it should allow you to add inputs my clicking the '+' icon
8. Configure any inputs and hit 'OK' when done, you should now have an AULab document with inputs and outputs

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-05-17 | New document that aU Lab only supports physical device singletons. |

