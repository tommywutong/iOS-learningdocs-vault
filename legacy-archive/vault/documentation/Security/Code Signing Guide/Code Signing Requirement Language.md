---
title: Code Signing Guide
apple_id: TP40005929
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Security
technology: Security
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/RequirementLang/RequirementLang.html
archived_at: '2026-07-18T02:06:16.761564Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Signing Guide](About%20Code%20Signing.md)


[Next](Document%20Revision%20History.md)[Previous](Code%20Signing%20Tasks.md)

# Code Signing Requirement Language

When you use the `codesign` command to sign a block of code, or Xcode does so on your behalf, you can optionally specify internal requirements; that is, the criteria that you recommend should be used to evaluate the code signature. At code signature evaluation time, the entity performing verification, usually a component of the operating system, decides whether to apply these internal requirements, or some other set of requirements, when deciding how to treat the signed code.

You use the code requirement language described in this chapter when specifying requirements to the `codesign` command (either on the command line, or as a step in the standard Xcode build process), or when using the `csreq` command, which is a tool that manipulates code requirements directly. For a complete enumeration of all the options available on each of these tools, see their respective man pages.

You can compile a set of requirements and save them in binary form using the `csreq` command. You can provide requirements to the `codesign` command either as source code or as a binary file. Both the `codesign` and `csreq` commands can convert a binary requirement set to text. Although there is some flexibility in the source code syntax (for example, quotes can always be used around string constants but are not always required), conversion from binary to text always uses the same form:

- Parentheses are placed (usually only) where required to clarify operator precedence.
- String constants are quoted (usually only) where needed.
- Whether originally specified as constants or through file paths, certificate hashes are always returned as hash constants.
- Comments in the original source are not preserved in the reconstructed text.

Some basic features of the language syntax are:

- Expressions use conventional infix notation (that is, the operator is placed between the two entities being acted on; for example _quantity_ `<` _constant_).
- Keywords are reserved, but can be quoted to be included as part of ordinary strings.
- Comments are allowed in C, Objective C, and C++.
- Unquoted whitespace is allowed between tokens, but strings containing whitespace must be quoted.
- Line endings have no special meaning and are treated as whitespace.

A requirement constitutes an expression without side effects. Each requirement can have any number of subexpressions, each of which is evaluated with a Boolean (succeed-fail) result. There is no defined order of evaluation. The subexpressions are combined using logical operators in the expression to yield an overall Boolean result for the expression. Depending on the operators used, an expression can succeed even if some subexpressions fail. For example, the expression

```
anchor apple or anchor = "/var/db/yourcorporateanchor.cert"
```

succeeds if either subexpression succeeds—that is, if the code was signed either by Apple or by your company—even though one of the subexpressions is sure to fail.

If an error occurs during evaluation, on the other hand, evaluation stops immediately and the `codesign` or `csreq` command returns with a result code indicating the reason for failure.

This section describes the use of string, integer, hash-value, and binary constants in the code signing requirement language.

String constants must be enclosed by double quotes (`" "`) unless the string contains only letters, digits, and periods (.), in which case the quotes are optional. Absolute file paths, which start with a slash, do not require quotes unless they contain spaces. For example:

```
com.apple.mail                       // no quotes are required
"com.apple.mail"                     // quotes are optional
"My Company's signing identity"      // requires quotes for spaces and apostrophe
/Volumes/myCA/root.crt               // no quotes are required
"/Volumes/my CA/root.crt"            // space requires quotes
"/Volumes/my_CA/root.crt"            // underscore requires quotes
```

It’s never incorrect to enclose the string in quotes—if in doubt, use quotes.

Use a backslash to “escape” any character. For example:

```
"one \" embedded quote"              // one " embedded quote
"one \\ embedded backslash"          // one \ embedded backslash
```

The apostrophe, or single quote (') is not a special character, in the sense that it does not need to be escaped, but it must be enclosed in double quotes when present in a string constant, as in the `"My Company's signing identity"` example above.

Integer constants are written the same way that base ten integer constants are written in C. The language does not allow radix prefixes (such as `0x`) or leading plus or minus (`+` or `-`) signs.

Hash values are written either as a hexadecimal number in quotes preceded by an `H`, or as a path to a file containing a binary certificate. If you use the first form, the number must include the exact number of digits in the hash value. A SHA-1 hash (the only kind currently supported) requires exactly 40 digits; for example:

```
H"0123456789ABCDEFFEDCBA98765432100A2BC5DA"
```

You can use either uppercase or lowercase letters (`A..F` or `a..f`) in the hexadecimal numbers.

If you specify a file path, the compiler reads the binary certificate and calculates the hash for you. The compiled version of the requirement code includes only the hash; the certificate file and the path are not retained. If you convert the requirement back to text, you get the hexadecimal hash constant. The file path must point to a file containing an X.509 DER encoded certificate. No container forms (PKCS7, PKCS12) are allowed, nor is the OpenSSL "PEM" form supported.

There are currently no variables in the requirement language.

The requirement language includes the following logical operators, in order of decreasing precedence:

- `!` (negation)
- `and` (logical AND)
- `or` (logical OR)

These operators can be used to combine subexpressions into more complex expressions. The negation operator (`!`) is a unary prefix operator. The others are infix operators. Parentheses can be used to override the precedence of the operators.

Because the language is free of side effects, evaluation order of subexpressions is unspecified.

The requirement language includes the following comparison operators:

- `=` (equals)
- `<` (less than)
- `>` (greater than)
- `<=` (less than or equal to)
- `>=` (greater than or equal to)
- `exists` (value is present)

The value-present (`exists`) operator is a unary suffix operator. The others are infix operators.

There are no operators for non-matches (not equal to, not greater than, and so on). Use the negation operator (`!`) together with the comparison operators to make non-match comparisons.

All equality operations compare some value to a constant. The value and constant must be of the same type: a string matches a string constant, a data value matches a hexadecimal constant. The equality operation evaluates to `true` if the value exists and is equal to the constant. String matching uses the same matching rules as `CFString` (see _[CFString Reference](https://developer.apple.com/documentation/corefoundation/cfstring)_).

In match expressions (see [Info](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknltk), [Part of a Certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknltm), and [Entitlement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknlto)), substrings of string constants can be matched by using the `*` wildcard character:

- `value = *constant*` is `true` if the value exists and any substring of the value matches the constant; for example:

  - `thunderbolt = *under*`
  - `thunderbolt = *thunder*`
  - `thunderbolt = *bolt*`
- `value = constant*` is `true` if the value exists and begins with the constant; for example:

  - `thunderbolt = thunder*`
  - `thunderbolt = thun*`
- `value = *constant` is `true` if the value exists and ends with the constant; for example:

  - `thunderbolt = *bolt`
  - `thunderbolt = *underbolt`

If the constant is written with quotation marks, the asterisks must be outside the quotes. An asterisk inside the quotation marks is taken literally. For example:

- `"ten thunderbolts" = "ten thunder"*` is `true`
- `"ten thunder*bolts" = "ten thunder*"*` is `true`
- `"ten thunderbolts" = "ten thunder*"` is `false`

Inequality operations compare some value to a constant. The value and constant must be of the same type: a string matches a string constant, a data value matches a hexadecimal constant. String comparisons use the same matching rules as `CFString` with the [kCFCompareNumerically](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/kcfcomparenumerically) option flag; for example, `"17.4"` is greater than `"7.4"`.

The existence operator tests whether the value exists. It evaluates to `false` only if the value does not exist at all or is exactly the Boolean value `false`. An empty string and the number `0` are considered to exist.

Several keywords in the requirement language are used to require that specific certificates be present or other conditions be met.

The expression

`identifier =` _constant_

succeeds if the unique identifier string embedded in the code signature is exactly equal to _constant_. The equal sign is optional in identifier expressions. Signing identifiers can be tested only for exact equality; the wildcard character (`*`) can not be used with the identifier constraint, nor can identifiers be tested for inequality.

The expression

`info [`_key_`]`_match expression_

succeeds if the value associated with the top-level key in the code’s `info.plist` file matches _match expression_, where _match expression_ can include any of the operators listed in [Logical Operators](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknltg) and [Comparison Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknlti). For example:

```
info [CFBundleShortVersionString] < "17.4"
```

or

```
info [MySpecialMarker] exists
```

Specify _key_ as a string constant.

If the value of the specified key is a string, the match is applied to it directly. If the value is an array, it must be an array of strings and the match is made to each array element in turn, succeeding if any of them matches. Substrings of string constants can be matched by using any match expression (see [Comparison Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknlti)).

If the code has no `info.plist` file, or the `info.plist` does not contain the specified key, this expression evaluates to `false` without returning an error.

Certificate constraints refer to certificates in the certificate chain used to validate the signature. Most uses of the `certificate` keyword accept an integer that indicates the position of the certificate in the chain. Positive integers count from the leaf, the certificate that is part of the signer’s identity, toward the anchor, the certificate of the trusted certificate authority. Negative integers count backward from the anchor. For example, `certificate 1` is the intermediate certificate that was used to sign the leaf (that is, the signing certificate), which is itself `certificate 0`, while `certificate -2` indicates the certificate that was directly signed by the anchor, which is represented as `certificate -1`. This means that each certificate can be referenced in two different ways, depending on which way you count from, as shown in Table 4-1.

__Table 4-1__  Specifying relationships between anchor, intermediate, and leaf certificates using the certificate keyword

| Anchor | First intermediate | Second intermediate | Leaf |
| `certificate 3` | `certificate 2` | `certificate 1` | `certificate 0` |
| `certificate -1` | `certificate -2` | `certificate -3` | `certificate -4` |

For convenience, the following keywords are also defined:

- `certificate root`—the anchor certificate; same as `certificate -1`
- `anchor`—same as `certificate root`
- `certificate leaf`—the signing certificate; same as `certificate 0`

If there is no certificate at the specified position, the constraint evaluates to `false` without returning an error.

If the code was signed using an ad-hoc signature, there are no certificates at all and all certificate constraints evaluate to `false`. An ad-hoc signature is created by signing with the pseudo-identity `-` (a dash). An ad-hoc signature does not use or record a cryptographic identity, and thus identifies exactly and only the one program being signed.

If the code was signed by a self-signed certificate, the leaf and root refer to the same single certificate.

To require a particular certificate to be present in the certificate chain, use the form

`certificate` _position_ `=` _hash_

or one of the equivalent forms discussed above, such as `anchor =` _hash_. Hash constants are described in [Hash Constants](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknlte).

For Apple’s own code, signed by Apple, you can use the short form

`anchor apple`

For code signed by Apple, including code signed using a signing certificate issued by Apple to other developers, use the form

`anchor apple generic`

To match a well-defined element of a certificate, use the form

`certificate` _position_`[`_element_`]`_match expression_

where _match expression_ can include the `*` wildcard character and any of the operators listed in [Logical Operators](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknltg) and [Comparison Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknlti). The currently supported elements are given in Table 4-2.

__Table 4-2__  The elements of a certificate that can be matched using the certificate keyword

| Element name | Meaning | Comments |
| `subject.CN` | Subject common name | Shown in Keychain Access utility. |
| `subject.C` | Subject country name |  |
| `subject.D` | Subject description |  |
| `subject.L` | Subject locality |  |
| `subject.O` | Subject organization | Usually company or organization. |
| `subject.OU` | Subject organizational unit | In Apple issued developer certificates, this field contains the developer’s Team Identifier. |
| `subject.STREET` | Subject street address |  |

To check for the existence of any certificate field identified by its X.509 object identifier (OID), use the form

`certificate` _position_ `[field.`_OID_`] exists`

The object identifier must be written in numeric form (_x_`.`_y_`.`_z_...) and can be the OID of a certificate extension or of a conventional element of a certificate as defined by the CSSM standard. See Chapter 31 in _Common Security: CDSA and CSSM_, version 2 (with corrigenda) by the Open Group ([http://www.opengroup.org/security/cdsa.htm](http://www.opengroup.org/security/cdsa.htm)).

The expression

`certificate` _position_ `trusted`

succeeds if the certificate specified by _position_ is marked trusted for the code signing certificate policy in the system’s Trust Settings database. The _position_ argument is an integer or keyword that indicates the position of the certificate in the chain; see the discussion under [Certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknlts).

The expression

`anchor trusted`

succeeds if any certificate in the signature’s certificate chain is marked trusted for the code signing certificate policy in the system’s Trust Settings database, provided that no certificate closer to the leaf certificate is explicitly untrusted.

Thus, using the `trusted` keyword with a certificate position checks only the specified certificate, while using it with the `anchor` keyword checks all the certificates, giving precedence to the trust setting found closest to the leaf.

Certificates can have per-user trust settings and system-wide trust settings. In general, trust settings apply to specific policies. The `trusted` keyword in the code signing requirement language causes trust to be checked for the specified certificate or certificates for the user performing the validation. If there are no settings for that user, then the system settings are used. In all cases, only the trust settings for the code-signing policy are checked. Policies and trust are discussed in [Certificate, Key, and Trust Services](https://developer.apple.com/documentation/security/certificate_key_and_trust_services).

The expression

`entitlement [`_key_`]` _match expression_

succeeds if the value associated with the specified key in the signature’s embedded entitlement dictionary matches _match expression_, where _match expression_ can include the `*` wildcard character and any of the operators listed in [Logical Operators](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknltg) and [Comparison Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknlti). You must specify _key_ as a string constant. The entitlement dictionary is included in signatures for certain platforms.

The expression

`cdhash` _hash-constant_

computes the canonical hash of the program’s CodeDirectory resource and succeeds if the value of this hash exactly equals the specified hash constant.

The CodeDirectory resource is the master directory of the contents of the program. It consists of a versioned header followed by an array of hashes. This array consists of a set of optional special hashes for other resources, plus a vector of hashes for pages of the main executable. The CodeSignature and CodeDirectory resources together make up the signature of the code.

You can use the codesign utility with (at least) three levels of verbosity to obtain the hash constant of a program’s CodeDirectory resource:

```
    $ codesign -dvvv /bin/ls
    ...
    CodeDirectory v=20001 size=257 flags=0x0(none) hashes=8+2 location=embedded
    CDHash=4bccbc576205de37914a3023cae7e737a0b6a802
    ...
```

Because the code directory changes whenever the program changes in a nontrivial way, this test can be used to unambiguously identify one specific version of a program. When the operating system signs an otherwise unsigned program (so that the keychain or Parental Controls can recognize the program, for example), it uses this requirement.

A requirement set is a collection of distinct requirements, each indexed (tagged) with a type code. The expression

_tag_ `=>` _requirement_

applies _requirement_ to the type of code indicated by _tag_, where possible tags are:

- `host`—Applied to the direct host of this code module. Each code module in the hosting path can have its own host requirement, where the hosting path is the chain of code signing hosts starting with the most specific code known to be running, and ending with the root of trust (the kernel).
- `guest`—Applied to each code module that is hosted by this code module.
- `library`—Applied to all libraries mounted by the signed code.
- `designated`—An explicitly specified designated requirement for the signed code. If there is no explicitly specified designated requirement for the code, then there is no `designated` internal requirement.

The primary use of requirement sets is to represent the internal requirements of the signed code. For example:

```
    codesign -r='host => anchor apple and identifier com.apple.perl designated => anchor /my/root and identifier com.bar.foo'
```

sets the internal requirements of some code, having a host requirement of `anchor apple and identifier com.apple.perl` (“I'm a Perl script and I want to be run by Apple's Perl interpreter”) and an explicit designated requirement of `anchor /my/root and identifier com.bar.foo`. Note that this command sets no guest or library requirements.

You can also put the requirement set in a file and point to the file:

```
    codesign -r myrequirements.rqset
```

where the file `myrequirements.rqset` might contain:

```
    //internal requirements
      host => anchor apple and identifier com.apple.perl //require Apple's Perl interpreter
      designated => anchor /my/root and identifier com.bar.foo
```

[Next](Document%20Revision%20History.md)[Previous](Code%20Signing%20Tasks.md)

