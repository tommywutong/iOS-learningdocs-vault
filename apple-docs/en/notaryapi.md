---
title: Notary API
framework: Notary API
symbol_kind: module
role: collection
role_heading: Web Service
platforms: [Notary API 2.0.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/notaryapi
source_url: 'https://developer.apple.com/documentation/notaryapi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/notaryapi.json'
content_hash: 'sha256:2da96ed7d3742d92'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Notary API

<sub>Web Service</sub>

Submit your macOS software for notarization through a web interface.

## Overview

Notarization gives people confidence that your Developer ID-signed macOS software has been checked by Apple for malicious code. In addition to interacting with the notary service through Xcode or the `notarytool` command-line utility, you can bypass `notarytool` and interact directly with the service through its REST API. The Notary API is helpful for instances where you need to avoid a macOS dependency when uploading your app to the notary service, and provides endpoints that enable you to:

- Prepare the notary service to receive a new version of your software, and get credentials that you use to upload your software to an Amazon S3 endpoint.
- Check the status of a submission.
- Retrieve a log file that provides details about a submission.
- Get a list of your team’s previous submissions.

To learn how notarization works, see [Notarizing macOS software before distribution](security/notarizing-macos-software-before-distribution.md). For details about using the notary service REST API to upload your software, see [Submitting software for notarization over the web](notaryapi/submitting-software-for-notarization-over-the-web.md).

## Topics

### Essentials

- [Submitting software for notarization over the web](notaryapi/submitting-software-for-notarization-over-the-web.md) — Eliminate a dependency on macOS in your notarization workflow by interfacing directly with the notary service.

### Software submission

- [Submit Software](notaryapi/submit-software.md) — Start the process of uploading a new version of your software to the notary service.
- [NewSubmissionRequest](notaryapi/newsubmissionrequest.md) — Data that you provide when starting a submission to the notary service.
- [NewSubmissionResponse](notaryapi/newsubmissionresponse.md) — The notary service’s response to a software submission.

### Notarization results

- [Get Submission Status](notaryapi/get-submission-status.md) — Fetch the status of a software notarization submission.
- [SubmissionResponse](notaryapi/submissionresponse.md) — The notary service’s response to a request for the status of a submission.
- [Get Submission Log](notaryapi/get-submission-log.md) — Fetch details about a single completed notarization.
- [SubmissionLogURLResponse](notaryapi/submissionlogurlresponse.md) — The notary service’s response to a request for the log information about a completed submission.

### History

- [Get Previous Submissions](notaryapi/get-previous-submissions.md) — Fetch a list of your team’s previous notarization submissions.
- [SubmissionListResponse](notaryapi/submissionlistresponse.md) — The notary service’s response to a request for information about your team’s previous submissions.

### Errors

- [ErrorResponse](notaryapi/errorresponse.md) — The notary service’s response when an error occurs.
