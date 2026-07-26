---
title: 'createJob(destination:resource:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.1+（26.4 起废弃）, iPadOS 26.1+（26.4 起废弃）, Mac Catalyst 26.1+（26.4 起废弃）, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phassetresourceuploadjobchangerequest/createjob(destination:resource:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjobchangerequest/createjob(destination:resource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjobchangerequest/createjob%28destination%3Aresource%3A%29.json'
content_hash: 'sha256:6fc13d655e8c1172'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJobChangeRequest](../phassetresourceuploadjobchangerequest.md)

# createJob(destination:resource:)

<sub>Type Method</sub>

Creates an asset resource upload job.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func createJob(destination: URLRequest, resource: PHAssetResource)
```

## Discussion

- Parameter:

    - destination: the destination NSURLRequest to which this asset resource will be sent.
    - resource: the asset resource to be uploaded.

If the number of jobs exceeds [jobLimit](../phassetresourceuploadjob/joblimit.md) the photo library [- performChanges:completionHandler:](<../phphotolibrary/performchanges(__completionhandler_).md>) request will fail with a [limitExceeded](../phphotoserror-swift.struct/limitexceeded.md) error. To generate jobs after this limit is triggered, you must acknowledge succeeded/failed jobs, and wait for the registered/pending ones to finish uploading, which will make those jobs also succeeded/failed.
