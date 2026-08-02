---
title: Dictionary Services Programming Guide
apple_id: TP40006152
resource_type: Guide
platform: macOS
topic: User Experience
technology: CoreServices
published: '2007-05-30'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/DictionaryServicesProgGuide/access/access.html
archived_at: '2026-07-18T02:11:24.367653Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dictionary Services Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20Dictionaries.md)

# Accessing Dictionaries

Although the Dictionary Services programming interface provides only a few functions, these functions provide two valuable services. You can:

- Search for and obtain definitions from active dictionaries
- Display a Dictionary window that shows results of a dictionary search.

There are two steps you need to perform to get a definition:

1. Call the function [DCSGetTermRangeInString](https://developer.apple.com/documentation/coreservices/1450556-dcsgettermrangeinstring) to obtain the range in a dictionary that contains the definition for a word or phrase.
2. Pass that range to the function [DCSCopyTextDefinition](https://developer.apple.com/documentation/coreservices/1446842-dcscopytextdefinition) to get the definition associated with the text range and word or phrase. Dictionary Services returns the definition as a `CFString` object, which is plain text.

An alternative to getting the definition returned to you is to let Dictionary Services obtain and display the search results for you. In this case, instead of calling [DCSCopyTextDefinition](https://developer.apple.com/documentation/coreservices/1446842-dcscopytextdefinition), you would pass the text range to the `HIDictionaryWindowShow` function.

You may want to use the `HIDictionaryWindowShow` function to support contextual look-up in any application that provides text editing. For example, you could set up your application to respond as follows when the user control-clicks a text selection:

- Get the text selection and supply that as the `textString` parameter. If you use a `CFString` object for this text, you also need to specify a Core Text font to use to display the text. Otherwise, Dictionary Services uses the attributes provided.
- Determine the range of the selected text and provide that as the `selectionRange` parameter.
- Determine the origin of the typographic baseline of the selected text and provide that as the `textOrigin` parameter.

_Dictionary Services Reference_ describes functions and their parameters in detail.

[Next](Document%20Revision%20History.md)[Previous](Creating%20Dictionaries.md)

