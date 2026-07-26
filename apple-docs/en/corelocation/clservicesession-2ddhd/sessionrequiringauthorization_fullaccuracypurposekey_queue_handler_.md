---
title: 'sessionRequiringAuthorization:fullAccuracyPurposeKey:queue:handler:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clservicesession-2ddhd/sessionrequiringauthorization:fullaccuracypurposekey:queue:handler:'
source_url: 'https://developer.apple.com/documentation/corelocation/clservicesession-2ddhd/sessionrequiringauthorization:fullaccuracypurposekey:queue:handler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clservicesession-2ddhd/sessionrequiringauthorization%3Afullaccuracypurposekey%3Aqueue%3Ahandler%3A.json'
content_hash: 'sha256:f1f4d463418ff597'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLServiceSession](../clservicesession-2ddhd.md)

# sessionRequiringAuthorization:fullAccuracyPurposeKey:queue:handler:

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (CLServiceSession *) sessionRequiringAuthorization:(CLServiceSessionAuthorizationRequirement) authorizationRequirement fullAccuracyPurposeKey:(NSString *) purposeKey queue:(dispatch_queue_t) queue handler:(void (^)(CLServiceSessionDiagnostic *diagnostic)) handler;
```
