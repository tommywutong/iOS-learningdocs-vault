---
title: Search attribute keys and values
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/search-attribute-keys-and-values
source_url: 'https://developer.apple.com/documentation/security/search-attribute-keys-and-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/search-attribute-keys-and-values.json'
content_hash: 'sha256:6c5547fc1548e3e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [Keychain items](keychain-items.md)

# Search attribute keys and values

<sub>API Collection</sub>

Filter a keychain item search.

## Overview

When looking for items using any of the [SecItemCopyMatching](<secitemcopymatching(____).md>), [SecItemUpdate](<secitemupdate(____).md>), or [SecItemDelete](<secitemdelete(__).md>) functions, you specify a `query` dictionary containing both the item attributes to look for (see [Item attribute keys and values](item-attribute-keys-and-values.md)) and additional search attributes that condition the search. For example, you can use the matching key [kSecMatchLimit](ksecmatchlimit.md) with value [kSecMatchLimitOne](ksecmatchlimitone.md) to restrict the output to include only the first result even when more than one item matches.

## Topics

### Item search matching keys

- [kSecMatchPolicy](ksecmatchpolicy.md) — A key whose value indicates a policy with which a matching certificate or identity must verify.
- [kSecMatchItemList](ksecmatchitemlist.md) — A key whose value indicates a list of items to search.
- [kSecMatchSearchList](ksecmatchsearchlist.md) — A key whose value indicates a list of items to search.
- [kSecMatchIssuers](ksecmatchissuers.md) — A key whose value is a string to match against a certificate or identity’s issuers.
- [kSecMatchEmailAddressIfPresent](ksecmatchemailaddressifpresent.md) — A key whose value is a string to match against a certificate or identity’s email address.
- [kSecMatchSubjectContains](ksecmatchsubjectcontains.md) — A key whose value is a string to look for in a certificate or identity’s subject.
- [kSecMatchSubjectStartsWith](ksecmatchsubjectstartswith.md) — A key whose value is a string to match against the beginning of a certificate or identity’s subject.
- [kSecMatchSubjectEndsWith](ksecmatchsubjectendswith.md) — A key whose value is a string to match against the end of a certificate or identity’s subject.
- [kSecMatchSubjectWholeString](ksecmatchsubjectwholestring.md) — A key whose value is a string to exactly match a certificate or identity’s subject.
- [kSecMatchCaseInsensitive](ksecmatchcaseinsensitive.md) — A key whose value is a Boolean indicating whether case-insensitive matching is performed.
- [kSecMatchDiacriticInsensitive](ksecmatchdiacriticinsensitive.md) — A key whose value is a Boolean indicating whether diacritic-insensitive matching is performed.
- [kSecMatchWidthInsensitive](ksecmatchwidthinsensitive.md) — A key whose value is a Boolean indicating whether width-insensitive matching is performed.
- [kSecMatchTrustedOnly](ksecmatchtrustedonly.md) — A key whose value is a Boolean indicating whether untrusted certificates should be returned.
- [kSecMatchValidOnDate](ksecmatchvalidondate.md) — A key whose value indicates the validity date.
- [kSecMatchLimit](ksecmatchlimit.md) — A key whose value indicates the match limit.

### Match limit values

- [kSecMatchLimitOne](ksecmatchlimitone.md) — A value that corresponds to matching exactly one item.
- [kSecMatchLimitAll](ksecmatchlimitall.md) — A value that corresponds to matching an unlimited number of items.

### Additional item search keys

- [kSecUseItemList](ksecuseitemlist.md) — A key whose value is an array of items to search. _(deprecated)_
- [kSecUseKeychain](ksecusekeychain.md) — A key whose value is a keychain to operate on.
- [kSecUseOperationPrompt](ksecuseoperationprompt.md) — A key whose value is an operation prompt. _(deprecated)_
- [kSecUseNoAuthenticationUI](ksecusenoauthenticationui.md) — A key whose value is a Boolean indicating whether to disallow UI authentication. _(deprecated)_
- [kSecUseAuthenticationUI](ksecuseauthenticationui.md) — A key whose value indicates whether the user is prompted for authentication.
- [kSecUseAuthenticationContext](ksecuseauthenticationcontext.md) — A key whose value indicates a local authentication context to use.
- [kSecUseDataProtectionKeychain](ksecusedataprotectionkeychain.md) — A key whose value indicates whether to treat macOS keychain items like iOS keychain items.

### UI authentication values

- [kSecUseAuthenticationUIAllow](ksecuseauthenticationuiallow.md) — A value that indicates user authentication is allowed. _(deprecated)_
- [kSecUseAuthenticationUIFail](ksecuseauthenticationuifail.md) — A value that indicates user authentication is disallowed. _(deprecated)_
- [kSecUseAuthenticationUISkip](ksecuseauthenticationuiskip.md) — A value that indicates items requiring user authentication should be skipped.
