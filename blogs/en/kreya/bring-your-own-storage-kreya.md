---
title: 'Bring your own storage | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/bring-your-own-storage/'
original_language: en
published: 2023-10-02
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:da3a5c90d2b6a8a0'
translated: false
---

> 原文：[Bring your own storage | Kreya](https://kreya.app/blog/bring-your-own-storage/)　·　Kreya Blog

First of all, bring your own storage means you have the freedom to choose which storage provider you want to use to store your data. Unlike Postman, Insomnia and other API clients, Kreya gives you an easy way to bring your own storage. Kreya intentionally stores the project data in readable text files in the location of your choice, so you can easily read, edit, and share/sync the files with your favorite tools.

## Overview

Most of the data in a Kreya project is stored in JSON files. This blog post gives you an overview of the storage locations, the considerations behind the decisions and ways to share your Kreya projects with your colleagues.

## Structure of the Kreya storage

Operations (e.g. a REST call like "GET /books") are at the core of Kreya. An operation typically consists of one or multiple requests and one or multiple responses. In addition there are details such as metadata/headers, authentication and other settings.

Each time you click on an operation in Kreya, it's data is loaded from the file system. So far so good, but what does it look like on the file system?

A Kreya project is stored in a folder on the file system. To illustrate this, we will take the [example project from our GitHub repository](https://github.com/riok/Kreya/) and the simple `Say hello (unary call)` gRPC operation.

### Operation

All the details of this operation are stored in the `.krop` file.

The content of this file is in JSON format and contains the details such as the gRPC method name, metadata, request information, authentication, type and importer references.

```json
{  "details": {    "methodFqn": "kreya.ExampleService.SayHello",    "metadata": [      {        "key": "HOSTNAME",        "value": "MY_HOST"      }    ]  },  "requests": [    {      "location": "Say hello (unary call)-request.json"    }  ],  "authId": "f5650324-adf4-414c-81cc-d03dfbad08ae",  "operationType": "unary",  "invokerName": "grpc",  "importStreamId": "463869a1-4cf8-470d-871d-c873192881c7"}
```

### Request

The request is stored in a separate file within the same folder and is referenced from the operation file. We could have stored the request contents directly inside the operation file, but decided not to.

It would result in JSON, or any other request content such as XML or YAML, being stored in a string, which in turn would make syncing via Git less suitable (the diffs of JSON in a string look ugly and would produce a lot more merge conflicts). The loss of user formatting would also be a problem.

Unsurprisingly, the content of this file is the same as you can see in the request tab in Kreya.

```json
{  "name": "{{ faker.name.first_name }}"}
```

You may have noticed that there is no response file for this operation in this folder. This is intentional, as we wanted to be able to easily synchronise the entire Kreya project folder, and that's why responses need to be stored elsewhere. This also applies to all other user-specific data such as theme settings, user variables, active environment and so on. This data is stored in a small SQLite database in your application data folder.

### Project data

The project-wide information is stored in the `.krproj` file in the root folder of the project.

The content is also in JSON format and includes details of [import streams](https://kreya.app/docs/importers/), [auth configs](https://kreya.app/docs/authentication/) and [certificates](https://kreya.app/docs/ssl-tls/#tls-client-certificates).

```json
{  "id": "3f2f4cdb-b421-4355-b02b-27ccd1569e12",  "importStreams": [    {      "id": "463869a1-4cf8-470d-871d-c873192881c7",      "name": "gRPC server reflection importer",      "importerName": "GrpcServerReflection",      "createMissingOperations": false,      "options": {        "endpoint": "https://example-api.kreya.app:9090"      }    }  ],  "authConfigs": [    {      "name": "myAuth",      "providerName": "basic",      "id": "f5650324-adf4-414c-81cc-d03dfbad08ae",      "options": {        "username": "my-user-name",        "password": "{{ env.basic_auth_password }}"      }    }  ],  "certificates": []}
```

The same goes for [default and directory settings](https://kreya.app/docs/default-settings/) (`.krpref`) and [environments](https://kreya.app/docs/environments/) (`.krenv`). You'll probably get the point, and we don't need to go into detail for these two file types.

One point worth mentioning is the storage of passwords and other secrets. Since everything in a Kreya project is intended to be shared, passwords would also be shared. That is why we implemented "User specific data" in the [Environments](https://kreya.app/docs/environments/) feature, which are stored locally in your appdata folder and can be referenced almost everywhere.

## Sharing your project

Now that you know how Kreya stores your data, you may understand why it's so easy to share the project with others. Everything is file based and human readable. A Kreya project can be stored in a Git repository, a Dropbox/OneDrive/Google Drive folder or whatever your favorite tool for syncing files is.

A huge advantage with being able to sync the files via Git is that Kreya files can live side by side with a project's source code in the same Git repository. Try it for yourself! Create a Kreya project, upload it and start collaborating with your colleagues.

## Privacy

All the data is yours! As you can see, every file is stored on your drive and when you decide to share it with others, the control is in your hands.

## Bring your own storage or paid file sync?

Many of our competitors offer paid file sync as part of their core offering. We may have shot ourselves in the foot here: Since users can sync their Kreya projects with their own tools, they (probably) don't need an integrated file sync in Kreya, which we could offer for a monthly fee. However, we stand by this decision, even if it means less money for us. We may consider offering an optional, managed file sync in the future (in addition to the locally stored files), if there is demand from our users.

Write us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#88e0ede4e4e7c8e3faedf1e9a6e9f8f8) for any feedback or just to say hello. ✌
