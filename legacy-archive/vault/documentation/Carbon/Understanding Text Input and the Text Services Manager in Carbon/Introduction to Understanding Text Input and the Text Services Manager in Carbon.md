---
title: Understanding Text Input and the Text Services Manager in Carbon
apple_id: TP40000957
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-09-30'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/UnderstandTextInput_TSM/tinptsm_intro/tinptsm_intro.html
archived_at: '2026-07-15T05:24:42.272970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Understanding%20Text%20Input%20and%20the%20Text%20Services%20Manager.md)

# Introduction to Understanding Text Input and the Text Services Manager in Carbon

The _Text Services Manager_ (“TSM”) provides an environment for applications to use non-application-specific text services. The Text Services Manager handles communication between client applications that request text services and the software modules, known as text service components, that provide them. The Text Services Manager exists so that these two types of programs can work together without needing to know anything about one anothers’ internal structures or identities. The Text Services Manager presents separate programming interfaces to the features it provides for client applications and for text service components.

A _client application_ is a text-processing program that uses the Text Services Manager to request a service from a text service component. To accomplish this, a client application needs to make specific Text Services Manager calls during execution.

A _text service component_ is a utility program that uses the Text Services Manager to provide a text service to an application. Text service components are registered components with the Component Manager. Text services can include many different types of specific text-handling tasks, including spell-checking, hyphenation, and handling the input of complex text.

The most prevalent category of text services are those that handle the entry of complex text, that is, _input methods_. A typical example of an input method is a service that converts keyboard input into text that cannot be directly entered via a keyboard. Text input in Japanese, Chinese, Korean, or Unicode usually requires an input method.

Note that application support for full Unicode input depends on the application’s adoption of the Text Services Manager. Applications that do not adopt the Text Services Manager’s input model only receive text input from partial Unicode sources, that is, only those input sources whose output can be converted to a given Mac encoding.

[Next](Understanding%20Text%20Input%20and%20the%20Text%20Services%20Manager.md)

