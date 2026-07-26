---
title: Working with Asynchronous Objective-C APIs in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/01/result-init-helper/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bfa3e1277cc55366'
translated: false
---

> 原文：[Working with Asynchronous Objective-C APIs in Swift](https://oleb.net/blog/2017/01/result-init-helper/)　·　Ole Begemann

# Working with Asynchronous Objective-C APIs in Swift

Many asynchronous Objective-C APIs pass you two optional values in their completion handler: one for the method’s result if the operation was a success, and an error value in case the operation failed.

An example is the [`CLGeocoder.reverseGeocodeLocation`](https://developer.apple.com/reference/corelocation/clgeocoder/1423621-reversegeocodelocation) method in the Core Location framework. It takes a [`CLLocation`](https://developer.apple.com/reference/corelocation/cllocation) object and sends the coordinates to a web service to turn them [into a readable address](https://en.wikipedia.org/wiki/Reverse_geocoding). When the network request completes, the method calls its completion block with an optional array of [`CLPlacemark`](https://developer.apple.com/reference/corelocation/clplacemark) objects and an optional [`Error`](https://developer.apple.com/reference/corelocation/clerror.code) value:

```
class CLGeocoder {
    ...
    func reverseGeocodeLocation(_ location: CLLocation,
        completionHandler: @escaping ([CLPlacemark]?, Error?) -> Void)
    ...
}
```

This pattern of returning a pair of optional success value and optional error is the most practical way to handle this kind of situation in an Objective-C API. If this were a Swift API with no requirement to be callable from Objective-C, you would design it differently, though.

# Two possible outcomes, four potential states

The problem with the current API is that the operation really has only _two_ possible outcomes: either the request succeeds and returns a result, or it fails and returns an error. However, the code as it is allows _four_ different states:

1. Result is non-`nil` and error is `nil`.
2. Error is non-`nil` and result is `nil`.
3. Both are non-`nil`.
4. Both are `nil`.

The documentation of the API can take care to explicitly preclude the last two cases, but as a user you can never really be sure that the documentation is correct.

# A better design using `Result`

In Swift you might design the same API like this:

```
class CLGeocoder {
    ...
    func reverseGeocode(location: CLLocation,
        completion: @escaping (Result<[CLPlacemark]>) -> Void)
    ...
}
```

The completion block now only receives one (non-optional) argument, which has the type `Result<…>`. `Result` is an enum that’s very similar to Swift’s [`Optional`](https://developer.apple.com/reference/swift/optional) type. The only difference is that it can also store an error value in the `failure` case, whereas `Optional` only has an associated value for its success case:

```
enum Result<T> {
    case success(T)
    case failure(Error)
}
```

`Result` is currently not part of the Swift standard library, but it will probably be added at some time. Until then, it’s trivial to define it yourself, or you can use the popular [antitypical/Result](https://github.com/antitypical/Result) library.^[1](#fn:1)

With this fictional new API, the compiler could guarantee that the argument that gets passed to the completion block can only ever have two states, success or failure. You wouldn’t have to worry about the possibility that both values are present or both absent.

# An initializer to turn `(T?, Error?)` into `Result<T>`

However, we can’t change Apple’s APIs, so there’s nothing we can do about the inherent ambiguity in the completion block’s arguments. What we _can_ do is to contain the logic how to convert an optional success value and an optional error into a single `Result` value in one place. I do this in my code with a convenience initializer for `Result`:

```
import Foundation // needed for NSError

extension Result {
    /// Initializes a Result from an optional success value
    /// and an optional error. Useful for converting return
    /// values from many asynchronous Apple APIs to Result.
    init(value: T?, error: Error?) {
        switch (value, error) {
        case (let v?, _):
            // Ignore error if value is non-nil
            self = .success(v)
        case (nil, let e?):
            self = .failure(e)
        case (nil, nil):
            let error = NSError(domain: "ResultErrorDomain", code: 1,
                userInfo: [NSLocalizedDescriptionKey:
                    "Invalid input: value and error were both nil."])
            self = .failure(error)
        }
    }
}
```

In the case where both inputs are `nil` (which normally should never happen) this creates a custom error to put into the result. I use [`NSError`](https://developer.apple.com/reference/foundation/nserror) for this, but you could use any type that conforms to the `Error` protocol.

Having defined this initializer, I use the geocoding API like this:

```
let location = ...
let geocoder = CLGeocoder()
geocoder.reverseGeocodeLocation(location) { placemarks, error in
    // Turn arguments into Result
    let result = Result(value: placemarks, error: error)
    // Only work with result from here
    switch result {
    case .success(let p): ...
    case .failure(let e): ...
    }
}
```

It’s just one additional line to turn the arguments into a `Result` value, and from then on I don’t have to worry about unhandled cases anymore.

**Update January 20, 2017:** [Shawn Throop suggested](https://twitter.com/shawnthroop/status/822414872285679616) to add the better API I outlined above to `CLGeocoder` in an extension. Your code would then only call the `Result`-based method, which in turn calls the original API and takes care of the conversion:

```
extension CLGeocoder {
    func reverseGeocode(location: CLLocation,
        completion: @escaping (Result<[CLPlacemark]>) -> Void) {
        reverseGeocodeLocation(location) { placemarks, error in
            completion(Result(value: placemarks, error: error))
        }
    }
}
```

1. That `Result` type is slightly different than the one I use here: it uses strongly-typed errors, i.e. it has a second generic parameter for the type of the error value. [↩︎](#fnref:1)
