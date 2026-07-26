---
title: Randomization Services
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/randomization-services
source_url: 'https://developer.apple.com/documentation/security/randomization-services'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/randomization-services.json'
content_hash: 'sha256:a528be1046581675'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# Randomization Services

<sub>API Collection</sub>

Generate cryptographically secure random numbers.

## Overview

Many security operations rely on randomization to avoid reproducibility. This is true for many complex cryptographic operations, such as key generation, but is also true for something as simple as generating a password string that can’t be easily guessed. If the string’s characters are truly random (and kept hidden), an attacker has no choice but to try every possible combination one at a time in a brute force attack. For sufficiently long strings, this becomes unfeasible.

But the strength of such a password depends on the quality of the randomization. True randomization is not possible in a deterministic system, such as one where software instructions from a bounded set are executed according to well-defined rules. But even “good” randomization (in a statistical sense) is difficult to produce under these conditions. If an attacker can infer patterns in insufficiently randomized data, your system becomes compromised. Use randomization services to generate a cryptographically secure set of random numbers.

![Diagram showing random number generation.](../../../attachments/32623e7b9e864d13451c7d411afe7de1/media-2903623@2x.png)

## Topics

### Random Numbers

- [SecRandomCopyBytes](<secrandomcopybytes(______).md>) — Generates an array of cryptographically secure random bytes.
- [SecRandomRef](secrandomref.md) — An abstract Core Foundation-type object containing information about a random number generator.
- [kSecRandomDefault](ksecrandomdefault.md) — An alias for the default random number generator.
