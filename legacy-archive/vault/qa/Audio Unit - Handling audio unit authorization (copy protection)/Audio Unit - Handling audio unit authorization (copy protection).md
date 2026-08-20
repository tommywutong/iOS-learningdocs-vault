---
title: Audio Unit - Handling audio unit authorization (copy protection)
apple_id: DTS40010314
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2010-09-13'
source_url: https://developer.apple.com/library/archive/qa/qa1720/_index.html
archived_at: '2026-07-18T02:34:27.429104Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1720

# Audio Unit - Handling audio unit authorization (copy protection)

## Q:  How should an audio unit handle authorization requirements?

A: How should an audio unit handle authorization requirements?

If an audio unit provides a level of copy protection and is not authorized to run, the error code `kAudioUnitErr_Unauthorized` should be returned when an attempt is made to open or initialize the component.

Audio Unit Host applications such as AULab specifically check for `kAudioUnitErr_Unauthorized` and will present the user with a dialog asking if they would like to authorize the audio unit. This mechanism allows displaying an audio unit's custom user interface which should contain interface elements for handling the authorization process as required.

__Figure 1__  AULab's Authorization Check.

!

Once an audio unit has successfully been added to a graph and initialized no formal mechanism exists in the AU specification to handle dynamic de-authorization. For example, an audio unit may become unauthorized due to the removal of a hardware dongle. In these dynamic cases, the audio unit should either output silence, degrade audio quality or present some user feedback in the audio unit's user interface asking the user to reauthorize the audio unit.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-09-13 | New document that describes how to handle audio unit authorization requirements and the use of kAudioUnitErr_Unauthorized. |

