---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ErrorCodes.html
archived_at: '2026-07-15T07:23:32.749399Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Error Codes

This table contains the server errors that may occur when posting requests. The error codes appear in the response.

| Error | Description | HTTP status code |
| --- | --- | --- |
| `ACCESS_DENIED` | You don’t have permission to access the endpoint, record, zone, or database. | 403 |
| `ATOMIC_ERROR` | An atomic batch operation failed. | 400 |
| `AUTHENTICATION_FAILED` | Authentication was rejected. | 401 |
| `AUTHENTICATION_REQUIRED` | The request requires authentication but none was provided. | 421 |
| `BAD_REQUEST` | The request was not valid. | 400 |
| `CONFLICT` | The `recordChangeTag` value expired. (Retry the request with the latest tag.) | 409 |
| `EXISTS` | The resource that you attempted to create already exists. | 409 |
| `INTERNAL_ERROR` | An internal error occurred. | 500 |
| `NOT_FOUND` | The resource was not found. | 404 |
| `QUOTA_EXCEEDED` | If accessing the public database, you exceeded the app’s quota. If accessing the private database, you exceeded the user’s iCloud quota. | 413 |
| `THROTTLED` | The request was throttled. Try the request again later. | 429 |
| `TRY_AGAIN_LATER` | An internal error occurred. Try the request again. | 503 |
| `VALIDATING_REFERENCE_ERROR` | The request violates a validating reference constraint. | 412 |
| `ZONE_NOT_FOUND` | The zone specified in the request was not found. | 404 |

[Types and Dictionaries](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlte)

[Data Size Limits](PropertyMetrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrtfvjvomi)
