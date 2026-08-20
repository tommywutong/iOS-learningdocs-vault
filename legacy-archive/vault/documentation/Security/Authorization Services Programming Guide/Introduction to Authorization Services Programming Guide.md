---
title: Authorization Services Programming Guide
apple_id: TP30000995
resource_type: Guide
platform: macOS
topic: Security
technology: Security
published: '2011-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html
archived_at: '2026-07-18T02:06:31.835693Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Authorization%20Concepts.md)

# Introduction to Authorization Services Programming Guide

Authorization Services defines a programming interface that facilitates fine-grain control of _privileged operations_, such as accessing restricted areas of the operating system and self-restricted parts of your Mac app. This document describes how to use Authorization Services to control these privileged operations.

_Authorization Services Programming Guide_ explains the concepts behind authorization and provides examples of how to use Authorization Services.

Types of products that benefit from using Authorization Services include

- applications that call system-restricted tools
- software that restricts access to its own tools
- software installers that install privileged tools or require access to restricted areas of the operating system

For example, you can use Authorization Services to restart background processes or to gain access to restricted directories, such as the `/Applications` directory. Using Authorization Services properly in these situations greatly minimizes the possibility of your software inadvertently damaging restricted areas of the operating system, or allowing an unauthorized user access to these areas.

Your application can benefit from Authorization Services if it includes tools or performs operations to which you want only administrative users to have access.

Authorization Services uses the authentication mechanism in macOS. If future versions of macOS support additional authentication mechanisms, adopting Authorization Services now will enable your application to take advantage of these mechanisms with no change to your code.

[Authorization Concepts](Authorization%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqguwviubz) introduces you to authorization in macOS and describes the difference between authorization and authentication. This chapter explores scenarios that use Authorization Services. Read this chapter to better understand whether your software could benefit from using Authorization Services.

[Authorization Services Tasks](Authorization%20Services%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqgywviubz) explains in detail how to use Authorization Services in self-restricting applications, system-restricting applications, and privileged installers.

[Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojvfvbuqmrqhawviubr) defines new terms introduced in this book.

See [Authorization Services](https://developer.apple.com/documentation/security/authorization_services) for details about the API.

[Next](Authorization%20Concepts.md)

