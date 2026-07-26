---
title: About Imported Cocoa Error Parameters
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/about-imported-cocoa-error-parameters
source_url: 'https://developer.apple.com/documentation/swift/about-imported-cocoa-error-parameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/about-imported-cocoa-error-parameters.json'
content_hash: 'sha256:235b53a16535698e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Cocoa Design Patterns](cocoa-design-patterns.md)

# About Imported Cocoa Error Parameters

<sub>Article</sub>

Learn how Cocoa error parameters are converted to Swift throwing methods.

## Overview

In Cocoa, methods that produce errors take an [NSError](../foundation/nserror.md) pointer parameter as their last parameter, which populates its argument with an [NSError](../foundation/nserror.md) object if an error occurs. Swift automatically translates Objective-C methods that produce errors into methods that throw an error according to Swift’s native error handling functionality.

### Understand How Error Parameters Are Imported

Swift examines Objective-C method declarations and translates them into Swift throwing methods, with shorter names when possible.

For example, consider the [removeItem(at:)](<../foundation/filemanager/removeitem(at_).md>) method from [FileManager](../foundation/filemanager.md). In Objective-C, it’s declared like this:

```occ
- (BOOL)removeItemAtURL:(NSURL *)URL
                  error:(NSError **)error;
```

In Swift, it’s imported like this:

```swift
func removeItem(at: URL) throws
```

Notice that the [removeItem(at:)](<../foundation/filemanager/removeitem(at_).md>) method is imported by Swift with a `Void` return type, no error parameter, and a `throws` declaration.

If the last non-block parameter of an Objective-C method is of type `NSError **`, Swift replaces it with the throws keyword, to indicate that the method can throw an error. If the Objective-C method’s error parameter is also its first parameter, Swift attempts to simplify the method name further, by removing the `WithError` or `AndReturnError` suffix, if present, from the first part of the selector. If another method is declared with the resulting selector, the method name is not changed.

If an error producing Objective-C method returns a [BOOL](../objectivec/bool.md) value to indicate the success or failure of a method call, Swift changes the return type of the function to `Void`. Similarly, if an error producing Objective-C method returns a `nil` value to indicate the failure of a method call, Swift changes the return type of the function to a nonoptional type.

Otherwise, if no convention can be inferred, the method is left intact.

> [!note] Note
> You use the `NS_SWIFT_NOTHROW` macro on Objective-C method declarations that produce an [NSError](../foundation/nserror.md) to prevent it from being imported by Swift as a method that throws.

## See Also

### Common Patterns

- [Using Key-Value Observing in Swift](using-key-value-observing-in-swift.md) — Notify objects about changes to the properties of other objects.
- [Using Delegates to Customize Object Behavior](using-delegates-to-customize-object-behavior.md) — Respond to events on behalf of a delegator.
- [Managing a Shared Resource Using a Singleton](managing-a-shared-resource-using-a-singleton.md) — Provide access to a shared resource using a single, shared class instance.
- [Handling Cocoa Errors in Swift](handling-cocoa-errors-in-swift.md) — Throw and catch errors that use Cocoa’s error types.
