---
title: Payment Token Format Reference
apple_id: TP40014929
resource_type: Guide
platform: iOS
topic: null
technology: PassKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/PassKit/Reference/PaymentTokenJSON/PaymentTokenJSON.html
archived_at: '2026-07-27T06:57:09.286990Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Document%20Revision%20History.md)

# Payment Token Format Reference

A payment token is created by the Secure Element based on a payment request. The payment token has a nested structure, as shown in Figure 1-1.

__Figure 1-1__  Structure of a payment token

（原归档配图获取待重试：`payment_data_structure_2x.png`）

The Secure Element encrypts the token’s payment data using either elliptic curve cryptography (ECC) or RSA encryption. The encryption algorithm is selected by the Secure Element based on the payment request. Most regions use ECC encryption. RSA is used only in regions where ECC encryption is unavailable due to regulatory concerns.

## Top-Level Structure

The [paymentData](https://developer.apple.com/documentation/passkit/pkpaymenttoken/1617000-paymentdata) property of [PKPaymentToken](https://developer.apple.com/documentation/passkit/pkpaymenttoken) contains a UTF-8 serialization of a plain-text JSON dictionary with the following keys and values:

| Key | Value | Description |
| --- | --- | --- |
| `data` | payment data dictionary, Base64 encoded as a string | Encrypted payment data. |
| `header` | header dictionary | Additional version-dependent information used to decrypt and verify the payment. |
| `signature` | detached PKCS #7 signature, Base64 encoded as string | Signature of the payment and header data. The signature includes the signing certificate, its intermediate CA certificate, and information about the signing algorithm. |
| `version` | string | Version information about the payment token.  The token uses `EC_v1` for ECC-encrypted data, and `RSA_v1` for RSA-encrypted data. |

To decrypt the encrypted payment data, do the following:

1. Verify the signature as follows:

   1. Ensure that the certificates contain the correct custom OIDs: 1.2.840.113635.100.6.29 for the leaf certificate and 1.2.840.113635.100.6.2.14 for the intermediate CA. The value for these marker OIDs doesn’t matter, only their presence.
   2. Ensure that the root CA is the Apple Root CA - G3. This certificate is available from [apple.com/certificateauthority](https://www.apple.com/certificateauthority/).
   3. Ensure that there is a valid X.509 chain of trust from the signature to the root CA. Specifically, ensure that the signature was created using the private key corresponding to the leaf certificate, that the leaf certificate is signed by the intermediate CA, and that the intermediate CA is signed by the Apple Root CA - G3.
   4. Validate the token’s signature:

      - __For ECC__ (`EC_v1`), ensure that the signature is a valid ECDSA signature (ecdsa-with-SHA256 1.2.840.10045.4.3.2) of the concatenated values of the `ephemeralPublicKey`, `data`, `transactionId`, and `applicationData` keys.
      - __For RSA__ (`RSA_v1`), ensure that the signature is a valid RSA signature (RSA-with-SHA256 1.2.840.113549.1.1.11) of the concatenated values of the `wrappedKey`, `data`, `transactionId`, and `applicationData` keys.
   5. Inspect the CMS signing time of the signature, as defined by section 11.3 of RFC 5652. If the time signature and the transaction time differ by more than a few minutes, it's possible that the token is a replay attack.
2. Use the value of the `publicKeyHash` key to determine which merchant public key was used by Apple, and then retrieve the corresponding merchant public key certificate and private key.
3. Restore the symmetric key:

   - __For ECC__ (`EC_v1`):

     1. Use the merchant private key and the ephemeral public key, to generate the shared secret using Elliptic Curve Diffie-Hellman (id-ecDH 1.3.132.1.12).
     2. Use the merchant identifier field (OID 1.2.840.113635.100.6.32) of the public key certificate and the shared secret, to derive the symmetric key using the key derivation function described in NIST SP 800-56A, section 5.8.1, with the following input values:

        | Input name | Value |
        | --- | --- |
        | Hash function | SHA-256 |
        | Z | The shared secret calculated above using ECDH. |
        | Algorithm ID | The byte (`0x0D`) followed by the ASCII string `"id-aes256-GCM"`. The first byte of this value is an unsigned integer that indicates the string’s length in bytes; the remaining bytes are a variable-length string. |
        | Party U Info | The ASCII string `"Apple"`. This value is a fixed-length string. |
        | Party V Info | The SHA-256 hash of your merchant ID string literal; 32 bytes in size.  You can derive Party V Info from your Payment Processing certificate in either of two ways.  Method 1:  The plaintext merchant ID is included in the UID field of the Common Name. Calculate the SHA-256 hash of that plaintext string. Use the result for Party V Info.  Method 2:  The hex encoded hash of the merchant ID is included in OID 1.2.840.113635.100.6.32. Hexadecimal-decode that hash string to produce the original (non-hex-encoded) 32 byte hash. Use the result for Party V Info. |
        | Supplemental Public and Private Info | Unused. |

        __Note:__ Because the SHA-256 hash function produces exactly the needed amount of key material, there is only one iteration of the key-derivation function’s loop.
   - __For RSA__ (`RSA_v1`), the symmetric key is encrypted by a merchant’s public key using the RSA/ECB/OAEPWithSHA256AndMGF1Padding algorithm. Use your RSA private key to decrypt the wrapped key blob and access the symmetric key.
4. Use the symmetric key to decrypt the value of the `data` key.

   - __For ECC__ (`EC_v1`), Decrypt the `data` key using AES–256 (id-aes256-GCM 2.16.840.1.101.3.4.1.46), with an initialization vector of 16 null bytes and no associated authentication data.
   - __For RSA__ (`RSA_v1`), Decrypt the `data` key using AES–128 (id-aes128-GCM 2.16.840.1.101.3.4.1.6), with an initialization vector of 16 null bytes and no associated authentication data.
5. Confirm that this payment has not yet been credited by verifying that a payment with the same `transactionId` has not been processed. For efficiency, consider only those payments whose transaction time is within the time window of the current `transactionId`, as determined in step 1.e.
6. Verify the transaction details:

   - Check that the `currencyCode` is as expected.
   - Check that the `transactionAmount` is correct, as compared with the total charge of the transaction.
   - Check that the `applicationData` field matches the hash of the data used in the original payment request, and that the data is correct. For example, check that an order number in the data from the original payment request is the order number to which this payment is being applied. See [applicationData](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619298-applicationdata) in [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest) for more information.
7. Use the decrypted payment data to process the payment.

   __Note:__ The exact procedure used to process the payment varies depending on your payment processor and payment network. Please contact your payment processor for the full details.

__Important:__ If the signature is invalid or any of the hashes don’t match, ignore the transaction.

## Header Keys

The header contains the following keys and values:

| Key | Value | Description |
| --- | --- | --- |
| `applicationData` | SHA–256 hash, hex encoded as a string | _Optional._ Hash of the [applicationData](https://developer.apple.com/documentation/passkit/pkpaymentrequest/1619298-applicationdata) property of the original [PKPaymentRequest](https://developer.apple.com/documentation/passkit/pkpaymentrequest) object. If the value of that property is `nil`, this key is omitted. |
| `ephemeralPublicKey` | X.509 encoded key bytes, Base64 encoded as a string | Ephemeral public key bytes.  `EC_v1` only. |
| `wrappedKey` | A Base64 encoded string | The symmetric key wrapped using your RSA public key.  `RSA_v1` only. |
| `publicKeyHash` | SHA–256 hash, Base64 encoded as a string | Hash of the X.509 encoded public key bytes of the merchant’s certificate. |
| `transactionId` | A hexadecimal identifier, as a string | Transaction identifier, generated on the device. |

## Payment Data Keys

After being decrypted, the encrypted payment data contains the following keys and values:

| Key | Value | Description |
| --- | --- | --- |
| `applicationPrimaryAccountNumber` | string | Device-specific account number of the card that funds this transaction. |
| `applicationExpirationDate` | date as a string | Card expiration date in the format _YYMMDD_. |
| `currencyCode` | string | ISO 4217 numeric currency code, as a string to preserve leading zeros. |
| `transactionAmount` | number | Transaction amount. |
| `cardholderName` | string | _Optional._ Cardholder name. |
| `deviceManufacturerIdentifier` | string | Hex-encoded device manufacturer identifier. |
| `paymentDataType` | string | Either `3DSecure` or, if using Apple Pay in China, `EMV`. |
| `paymentData` | payment data dictionary | Detailed payment data. |

## Detailed Payment Data Keys (3-D Secure)

| Key | Value | Description |
| --- | --- | --- |
| `onlinePaymentCryptogram` | A Base64 encoded string | Online payment cryptogram, as defined by 3-D Secure. |
| `eciIndicator` | string | _Optional._ ECI indicator, as defined by 3-D Secure.  The card network may add an ECI indicator to the card data. This indicator is then included in the payment token.  If you receive an ECI indicator, you must pass it on to your payment processor; otherwise, the transaction fails. |

## Detailed Payment Data Keys (EMV)

| Key | Value | Description |
| --- | --- | --- |
| `emvData` | EMV payment structure, Base64 encoded as a string | Output from the Secure Element.  (EMV is used only in China.) |
| `encryptedPINData` | The encrypted PIN as a hex encoded string | The PIN is encrypted using the bank’s key.  `RSA_v1` only. |

[Next](Document%20Revision%20History.md)
