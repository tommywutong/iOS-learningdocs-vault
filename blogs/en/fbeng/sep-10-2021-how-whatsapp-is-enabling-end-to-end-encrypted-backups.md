---
title: Sep 10, 2021 How WhatsApp is enabling end-to-end encrypted backups
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2021/09/10/security/whatsapp-e2ee-backups/'
original_language: en
published: 2021-09-10
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:51e13e504def54b8'
translated: false
---

> 原文：[Sep 10, 2021 How WhatsApp is enabling end-to-end encrypted backups](https://engineering.fb.com/2021/09/10/security/whatsapp-e2ee-backups/)　·　Meta Engineering — iOS

For years, in order to safeguard the privacy of people’s messages, WhatsApp has provided [end-to-end encryption](https://engineering.fb.com/2021/04/16/security/dit/) by default ​​so messages can be seen only by the sender and recipient, and no one in between. Now, we’re planning to give people the option to protect their WhatsApp backups using end-to-end encryption as well.

People can already back up their WhatsApp message history via cloud-based services like Google Drive and iCloud. WhatsApp does not have access to these backups, and they are secured by the individual cloud-based storage services.

But now, if people choose to enable end-to-end encrypted (E2EE) backups once available, neither WhatsApp nor the backup service provider will be able to access their backup or their backup encryption key.

## How E2EE backups work

### Generating encryption keys and passwords

To enable E2EE backups, we developed an entirely new system for encryption key storage that works with both iOS and Android. With E2EE backups enabled, backups will be encrypted with a unique, randomly generated encryption key. People can choose to secure the key manually or with a user password. When someone opts for a password, the key is stored in a Backup Key Vault that is built based on a component called a hardware security module (HSM) — specialized, secure hardware that can be used to securely store encryption keys. When the account owner needs access to their backup, they can access it with their encryption key, or they can use their personal password to retrieve their encryption key from the HSM-based Backup Key Vault and decrypt their backup.

The HSM-based Backup Key Vault will be responsible for enforcing password verification attempts and rendering the key permanently inaccessible after a limited number of unsuccessful attempts to access it. These security measures provide protection against brute-force attempts to retrieve the key. WhatsApp will know only that a key exists in the HSM. It will not know the key itself.

### Storing keys in the Backup Key Vault

WhatsApp’s front-end service, ChatD, handles client connections and client-server authentication, and will implement a protocol that sends the keys to the backups to and from WhatsApp’s servers. The client and HSM-based Backup Key Vault will exchange encrypted messages, the contents of which will not be accessible to ChatD itself.

The HSM-based Backup Key Vault will sit behind ChatD and provide highly available and secure storage for the encryption keys to the backups. The backups themselves will be generated as a continuous stream of data that is encrypted using symmetric encryption with the generated key. With E2EE backups enabled, upon being encrypted, a backup can then be stored off device (e.g., to iCloud or Google Drive).

WhatsApp serves over 2 billion people, and one of the core challenges of this product was to make sure the HSM-based Backup Key Vault operates reliably. To help ensure that the system is always available, the HSM-based Backup Key Vault service will be geographically distributed across multiple data centers to keep it up and running in case of a data center [outage](https://engineering.fb.com/2021/06/02/data-center-engineering/how-facebook-deals-with-pcie-faults-to-keep-our-data-centers-running-reliably/).

![WhatsApp end-to-end encrypted backups](https://engineering.fb.com/wp-content/uploads/2021/09/WhatsApp_E2EE-Backups_64-digit-encryption.jpeg?w=1024)

<sub>Backups can be end-to-end encrypted using a 64-digit encryption key.</sub>

![WhatsApp end-to-end encrypted backups](https://engineering.fb.com/wp-content/uploads/2021/09/WhatsApp_E2EE-Backups_user-password.jpeg?w=1024)

<sub>Backups can also be secured with a password, in which case the encryption key is saved to the HSM-based Backup Key Vault.</sub>

### The HSM-based Backup Key Vault and the encryption and decryption process

When the account owner uses a personal password to protect their end-to-end encrypted backup, the HSM-based Backup Key Vault will store and safeguard it.

When someone wants to retrieve their backup:

1. They enter their password, which is encrypted and then verified by the Backup Key Vault.
2. Once the password is verified, the Backup Key Vault will send the encryption key back to the WhatsApp client.
3. With the key in hand, the WhatsApp client can then decrypt the backups.

Alternatively, if an account owner has chosen to use the 64-digit key alone, they will have to manually enter the key themselves to decrypt and access their backups.

E2EE backups will be available on iOS and Android in the coming weeks. Check out the [end-to-end encrypted backups white paper](https://www.whatsapp.com/security/WhatsApp_Security_Encrypted_Backups_Whitepaper.pdf) to learn more about the technical details.
