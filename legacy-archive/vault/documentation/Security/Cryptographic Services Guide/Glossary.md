---
title: Cryptographic Services Guide
apple_id: TP40011172
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Glossary/Glossary.html
archived_at: '2026-07-18T02:06:48.071384Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cryptographic Services Guide](About%20Cryptographic%20Services.md)


[Next](Document%20Revision%20History.md)[Previous](CDSA%20Overview.md)

# Glossary

- __anchor certificate__

  A digital certificate trusted to be valid, which can then be used to verify other certificates. An anchor certificate can be a [root certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfeesskh), a cross-certified certificate (that is, a certificate signed with more than one [certificate chain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceivcuoscd)), or a locally defined source of trust.

- __CDSA__

  Abbreviation for Common Data Security Architecture. An open software standard for a security infrastructure that provides a wide array of security services, including fine-grained access permissions, authentication of users, encryption, and secure data storage. CDSA has a standard application programming interface, called [CSSM](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfaugssd). In addition, OS X includes its own security APIs that call the CDSA API for you.

- __certificate__

  See [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfduorcf).

- __certificate chain__

  See [chain of trust](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywvgvzr).

- __certificate extension__

  A data field in a [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfduorcf) containing information such as allowable uses for the certificate.

- __Certificate, Key, and Trust Services__

  An API you can use to create, manage, and read certificates; add certificates to a keychain; create encryption keys; and manage trust policies. In iOS, you can also use this API to encrypt, decrypt, and sign data.

- __certification authority (CA)__

  The issuer of a [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfduorcf). In order for the digital certificate to be trusted, the certification authority must be a trusted organization that authenticates an applicant before issuing a certificate.

- __chain of trust__

  A set of [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfduorcf)s in which each certificate signs the next certificate, ending in a [root certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfeesskh) that is also a trusted [anchor certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejjceuq2e). A chain of trust can be used to verify the validity of a digital certificate.

- __cipher__

  A scheme for encrypting data.

- __ciphertext__

  Text or other data that has been encrypted. Compare [cleartext](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywvgvzwhe).

- __cleartext__

  Ordinary, unencrypted data. Compare [ciphertext](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceivfeoq2k).

- __cryptographic hashing__

  The process whereby data is transformed into a much smaller value that can take the place of the original data for cryptographic purposes. A hashing algorithm takes any amount of data and transforms it into a fixed-size output value. For a cryptographic hash function to be useful for security, it has to be extremely difficult or impossible to reconstruct the original data from the hash value, and it must be extremely unlikely that the same output value could result from any similar input data. See also [message digest](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceizbeessd).

- __CSSM__

  Abbreviation for Common Security Services Manager. A public application programming interface for [CDSA](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceirceoqsh). CSSM also defines an interface for plug-ins that implement security services for a particular operating system and hardware environment.

- __decryption__

  The transformation of encrypted data back into the original cleartext. Compare [encryption](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceizbussch).

- __Diffie-Hellman key exchange__

  A protocol that provides a way for two ends of a communication session to generate a symmetric shared secret key through the exchange of public keys.

- __digest__

  See [message digest](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceizbeessd).

- __digital certificate__

  A collection of data used to verify the identity of the holder or sender of the certificate. OS X and iOS support the X.509 standard for digital certificates. See also [certificate chain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceivcuoscd).

- __digital signature__

  A way to ensure the integrity of a message or other data using public key cryptography. To create a digital signature, the signer generates a message digest of the data and then uses a private key to encrypt the digest. The signature includes the encrypted digest and identifies the signer. Anyone wanting to verify the signature uses the signer’s digital certificate, which contains the public key needed to decrypt the digest and specifies the algorithm used to create the digest.

- __encryption__

  The transformation of data into a form in which it cannot be made sense of without the use of some key. Such transformed data is referred to as _ciphertext_. Use of a key to reverse this process and return the data to its original (cleartext) form is called [decryption](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywvgvzrgm).

- __hash algorithm__

  See [cryptographic hashing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywvgvzrgi).

- __identity__

  A digital certificate together with an associated private key.

- __keychain__

  A database in OS X and iOS used to store encrypted passwords, private keys, and other secrets. It is also used to store certificates and other non-secret information that is used in cryptography and authentication. Apps can use the Keychain Services API (or the legacy Keychain Manager API) to manipulate data in the keychain. Users can also access keychain data using the Keychain Access utility.

- __man-in-the-middle attack__

  An attack on a communication channel in which the attacker can intercept messages going between two parties without the communicating parties’ knowledge. Typically, the man in the middle substitutes messages and even cryptographic keys to impersonate one party to the other.

- __message digest__

  The result of applying a cryptographic hash function to a message or other data. A cryptographically secure message digest cannot be transformed back into the original message and cannot (or is very unlikely to) be created from a different input. Message digests are used to ensure that a message has not been corrupted or altered. For example, they are used for this purpose in digital signatures. The digital signature includes a digest of the original message, and the recipient prepares their own digest of the received message. If the two digests are identical, then the recipient can be confident that the message has not been altered or corrupted.

- __plaintext__

  See [cleartext](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywvgvzwhe).

- __private key__

  A cryptographic key that must be kept secret, usually used in the context of public key cryptography. Although this term can also be used in the context of symmetric key cryptography, the term “secret key” (or “shared secret”) is preferred.

- __pseudorandom number__

  A number generated by an algorithm that produces a series of numbers with no discernible pattern. It should be impossible or nearly impossible to deduce the algorithm from such a series. However, unlike a truly random number generator, a pseudorandom number generator always produces the same series if the algorithm is given the same starting value or values.

- __public-private key pair__

  A pair of mathematically related keys that cannot be derived from one another used in public key cryptography. One of these keys (the [public key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejjdesqkb)) is made public while the other (the [private key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejbcekqsg)) is kept secure. Data encrypted with one key must be decrypted with the other.

- __public key__

  A cryptographic key that can be shared or made public without compromising the cryptographic method—generally, the public portion of a public-private key pair. See also [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceivbeoskk).

- __public key certificate__

  See [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfduorcf).

- __public key cryptography__

  A cryptographic method using a public-private key pair. If the public key is used to encrypt the data, only the holder of the private key can decrypt it; therefore the data is secure from unauthorized use. If the private key is used to encrypt the data, anyone with the public key can decrypt it. Because only the holder of the private key could have encrypted it, such data can be used for authentication. See also [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfduorcf); [digital signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejbdegrse). Compare [symmetric key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceirdeqrki).

- __root certificate__

  A [certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceivfegqsk) that can be verified without recourse to another certificate. Rather than being signed by a further certification authority (CA), a root certificate is verified using the widely available public key of the CA that issued the root certificate. Compare [anchor certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejjceuq2e).

- __root certification authority__

  The certification authority that owns the [root certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfeesskh).

- __RSA encryption__

  A system of public key cryptography, named for its inventors: Ron Rivest, Adi Shamir, and Leonard Adleman. The RSA algorithm takes two large prime numbers, finds their product, and then derives a [public-private key pair](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceivbeoqkb) from the prime numbers and their product. The strength of this algorithm depends on the difficulty of factoring the resulting product and upon reasonable assurance of the primality of the values used in constructing the keys.

- __secret key__

  A cryptographic key that cannot be made public without compromising the security of the cryptographic method. In symmetric key cryptography, a secret key is used both to encrypt and decrypt data, and is often called a _shared secret_. Although the term “secret key” can be used in the context of public key cryptography, the term “private key” is preferred.

- __Secure Sockets Layer (SSL)__

  A protocol that provides secure communication over a TCP/IP connection such as the Internet. It uses digital certificates for authentication and digital signatures to ensure message integrity, and can use public key cryptography to ensure data privacy. An SSL service negotiates a secure session between two communicating endpoints. SSL is built into all major browsers and web servers. SSL has been superseded by [Transport Layer Security (TLS)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceireeur2b).

- __secure storage__

  Storage of encrypted data on disk or another medium that persists when the power is turned off.

- __Secure Transport__

  The OS X and iPhone implementation of Secure Sockets Layer (SSL) and Transport Layer Security (TLS), used to create secure connections over TCP/IP connections such as the Internet. Secure Transport includes an API that is independent of the underlying transport protocol. The CFNetwork and URL Loading System APIs use the services of Secure Transport.

- __session key__

  A cryptographic key calculated or issued for use only for the duration of a specific communication session. Session keys are used, for example, by the SSL and Kerberos protocols, and are often obtained using [Diffie-Hellman key exchange](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceinbecrkj).

- __SSL__

  See [Secure Sockets Layer (SSL)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugscejfduurki).

- __strength__

  A measure of the amount of effort required to break a security system. For example, the strength of RSA encryption is believed to be related to the difficulty of factoring the product of two large prime numbers.

- __symmetric key cryptography__

  Cryptography that uses a single shared key to encrypt and decrypt data. See also [secret key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywvgvzthe). Compare [public key cryptography](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceivbeoskk).

- __TLS__

  See [Transport Layer Security (TLS)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqmrqgywugsceireeur2b).

- __Transport Layer Security (TLS)__

  A protocol that provides secure communication over a TCP/IP connection such as the Internet. It uses certificates for authentication and signatures to ensure message integrity, and can use public key cryptography to ensure data privacy. A TLS service negotiates a secure session between two communicating endpoints. TLS is built into recent versions of all major browsers and web servers. TLS is the successor to SSL. Although the TLS and SSL protocols are not interoperable, Secure Transport can back down to SSL 3.0 if a TLS session cannot be negotiated.

- __trust policy__

  A set of rules that specify the appropriate uses for a certificate based on its certificate extensions and other trust criteria. For example, a standard trust policy specifies that the user should be prompted for permission to trust an expired certificate. However, a custom trust policy might override that behavior in some specific set of circumstances, such as when verifying the signature on a document that you know was generated while the certificate was still valid.

- __X.509__

  A standard for digital certificates promulgated by the International Telecommunication Union (ITU). The X.509 ITU standard is widely used on the Internet and throughout the information technology industry for designing secure apps based on a public key infrastructure (PKI).

[Next](Document%20Revision%20History.md)[Previous](CDSA%20Overview.md)

