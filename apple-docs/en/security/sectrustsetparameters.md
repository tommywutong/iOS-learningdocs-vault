---
title: SecTrustSetParameters
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectrustsetparameters
source_url: 'https://developer.apple.com/documentation/security/sectrustsetparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetparameters.json'
content_hash: 'sha256:ee6eedd2da5ffabe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetParameters

<sub>Function</sub>

Sets the action and action data for a trust management object.

<sub>macOS</sub>

```objc
OSStatus SecTrustSetParameters(SecTrustRef trustRef, CSSM_TP_ACTION action, CFDataRef actionData);
```

## Parameters

- `trustRef` — The trust management object to which you want to add an action or set action data. A trust management object includes one or more certificates plus the policy or policies to be used in evaluating trust. Use the [SecTrustCreateWithCertificates](<sectrustcreatewithcertificates(______).md>) function to create a trust management object.

- `action` — A CSSM trust action. Pass `CSSM_TP_ACTION_DEFAULT` for the default action. Other actions available, if any, are described in the documentation for the trust policy module. For the AppleX509TP module, see the [Apple Trust Policy Module Functional Specification](https://developer.apple.com/library/archive/documentation/Security/Reference/SecAppleTrustPolicyModuleSpec/Apple_Trust_Policy_Module_Functional_Specification.pdf).

- `actionData` — A reference to action data. `CSSM_APPLE_TP_ACTION_FLAGS` lists possible values for this parameter for the AppleX509TP trust policy module’s default action. For other actions (if any), the possible values for the action data are specified in the [Apple Trust Policy Module Functional Specification](https://developer.apple.com/library/archive/documentation/Security/Reference/SecAppleTrustPolicyModuleSpec/Apple_Trust_Policy_Module_Functional_Specification.pdf).

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Before you call [SecTrustEvaluate](<sectrustevaluate(____).md>), you can optionally use this function to set one or more action flags or to set action data. Actions, where available, affect the trust evaluation for all policies being evaluated. For example, if you set the action data for the default action to `CSSM_TP_ACTION_ALLOW_EXPIRED`, then the `SecTrustEvaluate` function ignores the certificate’s expiration date and time.

It is safe to call this function concurrently on two or more threads as long as it is not used to change the value of a trust management object that is simultaneously being used by another function. For example, you cannot call this function on one thread at the same time as you are calling the [SecTrustEvaluate](<sectrustevaluate(____).md>) function for the same trust management object on another thread, but you can call this function and simultaneously evaluate a different trust management object on another thread. Similarly, calls to functions that return information about a trust management object (such as the [SecTrustCopyCustomAnchorCertificates](<sectrustcopycustomanchorcertificates(____).md>) function) may fail or return an unexpected result if this function is simultaneously changing the same trust management object on another thread.
