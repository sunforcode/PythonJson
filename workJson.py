jsonString = """
{
    "data": {
        "__schema": {
            "types": [
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Customer",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Address",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "addresses",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "assetUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "ApiKey",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "apiKeys",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Broker",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "broker",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Market",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "favouriteMarkets",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "identity",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "invitationCode",
                            "isDeprecated": false,
                            "description": "invitation code",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "LockedAsset",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "lockedAssets",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "assetUuid",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "ID",
                                        "kind": "SCALAR"
                                    },
                                    "name": "lockableId",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "LockableTypes",
                                        "kind": "ENUM"
                                    },
                                    "name": "lockableType",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Qualification",
                                "kind": "OBJECT"
                            },
                            "name": "qualification",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "scope",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "userId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "BannerKind",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "MOBILE",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "WEB",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AddQualificationPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Qualification",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "qualification",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "DateTime",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null

                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "SendPasswordResetEmailPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Market",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Asset",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "baseAsset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "baseAssetUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "baseScale",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "minQuoteValue",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Asset",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "quoteAsset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "quoteAssetUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "quoteScale",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "uuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "CreateSessionPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Session",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "session",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AddWithdrawalInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "gateway",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "memo",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "note",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "targetAddress",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UpdateAssetPinInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "originalPin",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "pin",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "TradingZone",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "index",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "Market",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "markets",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "title",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UpdateOtpInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "otpCode",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "otpSecret",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "password",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AddApiKeyInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "label",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "scopes",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "VerificationState",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "EMAIL_VERIFIED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "IDENTITY_APPROVED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "IDENTITY_DENIED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "IDENTITY_SUBMITTED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INITIAL",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Asset",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "chain",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "contractAddress",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "Gateway",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "gateways",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "grapheneAddresses",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isDepositEnabled",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isFiat",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isGraphene",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isStub",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isWithdrawalEnabled",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Logo",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "logo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "Payment",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "payments",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "scale",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "symbol",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "uuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "withdrawalFee",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "ID",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `ID` scalar type represents a unique identifier, often used torefetch an object or as key for a cache. The ID type appears in a JSONresponse as a String; however, it is not intended to be human-readable.When expected as an input type, any string (such as `4`) or integer(such as `4`) input value will be accepted as an ID."
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Payment",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "account",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Gateway",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "gateway",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "VerifyPasswordInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "password",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ResetAssetPinPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "VerifyPasswordPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Gateway",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "GatewayKind",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requiredConfirmations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "uuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "SendConfirmationEmailInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UpdateUserInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "locale",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AuthenticateCustomerPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Session",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "session",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "WithdrawalEdge",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "cursor",
                            "isDeprecated": false,
                            "description": "A cursor for use in pagination",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Withdrawal",
                                "kind": "OBJECT"
                            },
                            "name": "node",
                            "isDeprecated": false,
                            "description": "The item at the end of the edge",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ConfirmEmailPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Address",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Asset",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "asset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "use asset instead",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "chain",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customerId",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "remove in future",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "memo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "value",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "GatewayKind",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "BANK",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "CHAIN",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "WithdrawalState",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "CANCELLED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "COMPLETED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FAILED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "PENDING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "TRANSACTION_CREATED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "WITHHOLD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ResetPasswordPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UnlockAssetInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockableId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "LockableTypes",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockableType",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UpdateUserPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "String",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `String` scalar type represents textual data, represented as UTF-8character sequences. The String type is most often used by GraphQL torepresent free-form human-readable text."
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ResetOtpPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ResetOtpInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "otpCode",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "otpSecret",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "resetToken",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Trade",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "price",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OrderSide",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "takerSide",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ViewerSide",
                                "kind": "ENUM"
                            },
                            "name": "viewerSide",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "RemoveApiKeyInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ApiKeyWithSecret",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Customer",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customer",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "label",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "scopes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "secretKey",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "uuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "CreateSessionInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "email",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "otpCode",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "password",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "User",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetPinEnabled",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "credibility",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "email",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isTradeEnabled",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isWithdrawalEnabled",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "locale",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "mobile",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "nationCode",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "securityLevel",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "twoFactorEnabled",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "VerificationState",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "verificationState",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "SendPasswordResetEmailInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "email",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "otpCode",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ResetAssetPinInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetPin",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "resetToken",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AddFavouriteMarketPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Market",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "market",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "RemoveFavouriteMarketPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Market",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "market",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Metadata",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "Application",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "applications",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "Banner",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "banners",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "BannerKind",
                                            "kind": "ENUM"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "kind",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "exchangeName",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "host",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hosts",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "signInUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "signOutUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "StaticFile",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "staticFiles",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "supportsCookieAuth",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "supportsPasswordAuth",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "supportsSsoAuth",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "tokenExpireSeconds",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "TradingZone",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "tradingZones",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "PageInfo",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "endCursor",
                            "isDeprecated": false,
                            "description": "When paginating forwards, the cursor to continue.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hasNextPage",
                            "isDeprecated": false,
                            "description": "When paginating forwards, are there more items?",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hasPreviousPage",
                            "isDeprecated": false,
                            "description": "When paginating backwards, are there more items?",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "startCursor",
                            "isDeprecated": false,
                            "description": "When paginating backwards, the cursor to continue.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "TradeEdge",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "cursor",
                            "isDeprecated": false,
                            "description": "A cursor for use in pagination",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Trade",
                                "kind": "OBJECT"
                            },
                            "name": "node",
                            "isDeprecated": false,
                            "description": "The item at the end of the edge",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UpdatePasswordPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AddWithdrawalPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "WithdrawalEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "edge",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "LockAssetPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "LockedAsset",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockedAsset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ViewerSide",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ASK",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "BID",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SELF_TRADING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Session",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Customer",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customer",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "token",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AddQualificationInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "scope",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Logo",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "default",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "white",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ApiKey",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Customer",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customer",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "label",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "scopes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "uuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "OtpSecret",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "secret",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "OrderSide",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ASK",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "BID",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Withdrawal",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Asset",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "asset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "use asset instead",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "DateTime",
                                "kind": "SCALAR"
                            },
                            "name": "completedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customerId",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "remove in future",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "explain",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "explorerUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "fee",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "feeAssetUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isInternal",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "note",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "recipientId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "WithdrawalState",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "state",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "targetAddress",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "txid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Broker",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "exchangeName",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "host",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hosts",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "signInUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "signOutUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "supportsCookieAuth",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "supportsPasswordAuth",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "supportsSsoAuth",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "tokenExpireSeconds",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UnlockAssetPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "LockedAsset",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockedAsset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UpdateOtpPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "StaticFile",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "StaticFileKind",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "url",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Invitee",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "email",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "DateTime",
                                "kind": "SCALAR"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "StaticFileKind",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "CONFIG_JSON",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "CSS",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Int",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Int` scalar type represents non-fractional signed whole numeric values.Int can represent values between `-(2^53 - 1)` and `2^53 - 1` since it isrepresented in JSON as double-precision floating point numbers specifiedby [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point)."
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "RemoveApiKeyPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ApiKey",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "apiKey",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "OneOperationEventForMobile",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "imageUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "link",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ResetPasswordInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "newPassword",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "resetToken",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "ConfirmEmailInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "bindToken",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "SendConfirmationEmailPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "RemoveFavouriteMarketInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AuthenticateCustomerInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "token",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AddApiKeyPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ApiKeyWithSecret",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "apiKey",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "LockedAsset",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Asset",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "asset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "balance",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockableId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "LockableTypes",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockableType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "LockAssetInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockableId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "LockableTypes",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockableType",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "LockableTypes",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "EVENT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "AddFavouriteMarketInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "CreateCustomerInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "email",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "invitationCode",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "locale",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "password",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "TradeConnection",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "TradeEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "edges",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Trade",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "nodes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "PageInfo",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "pageInfo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "OperationEvent",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "OneOperationEventForMobile",
                                "kind": "OBJECT"
                            },
                            "name": "one",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "CreateCustomerPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Customer",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customer",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "token",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Boolean",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Boolean` scalar type represents `true` or `false`."
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Banner",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "imageUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "index",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "BannerKind",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "linkUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "title",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Decimal",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Decimal` scalar type represents signed double-precision fractionalvalues parsed by the `Decimal` library.  The Decimal appears in a JSONresponse as a string to preserve precision."
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Application",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "Qualification",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isEnabled",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "scope",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "sequence",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "updatedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UpdateAssetPinPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "User",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "user",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "broker",
                    "possibleTypes": null,
                    "name": "UpdatePasswordInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "newPassword",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "originalPassword",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "otpCode",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__InputValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "defaultValue",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Type",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__EnumValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "enumValues",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Field",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "fields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "inputFields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "interfaces",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "ofType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "possibleTypes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents scalars, interfaces, object types, unions, enums in the system"
                },
                {
                    "possibleTypes": null,
                    "name": "__EnumValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Field",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Schema",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Directive",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "directives",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "mutationType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "queryType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "subscriptionType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "types",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a schema"
                },
                {
                    "possibleTypes": null,
                    "name": "__Directive",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__DirectiveLocation",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "locations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onField",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FIELD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onFragment",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FRAGMENT_SPREAD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onOperation",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value OPERATION",
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a directive"
                },
                {
                    "possibleTypes": null,
                    "name": "__DirectiveLocation",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "FIELD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_SPREAD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INLINE_FRAGMENT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MUTATION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "QUERY",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SUBSCRIPTION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "ActionPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "msg",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ActionState",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "state",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "ActionState",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "DONE",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FAILED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "PENDING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "AmountPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "accountName",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "staked",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "staking",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "unstaking",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Boolean",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Boolean` scalar type represents `true` or `false`."
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "Campaigns",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "TgGroup",
                                "kind": "OBJECT"
                            },
                            "name": "tgGroup",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "VipGroup",
                                "kind": "OBJECT"
                            },
                            "name": "vipGroup",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "CriterionPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "DateTime",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `DateTime` scalar type represents a date and time in the UTCtimezone. The DateTime appears in a JSON response as an ISO8601 formattedstring, including UTC timezone (Z). The parsed date and time string willbe converted to UTC and any UTC offset other than 0 will be rejected."
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "Decimal",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Decimal` scalar type represents signed double-precision fractionalvalues parsed by the `Decimal` library.  The Decimal appears in a JSONresponse as a string to preserve precision."
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "HistoryAction",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "STAKE",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "UNSTAKE",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "VOTE",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "HistoryStatus",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "CONFIRMED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FAILED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "UNCONFIRMED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Int",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Int` scalar type represents non-fractional signed whole numeric values.Int can represent values between `-(2^53 - 1)` and `2^53 - 1` since it isrepresented in JSON as double-precision floating point numbers specifiedby [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point)."
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "PollInfoPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "ballots",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "choice",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isPollOpen",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "PollStatus",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "FAILED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SUCCEEDED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "PollVotePayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "PollStatus",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "status",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "ProducerAdPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "position",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "url",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "ProducerPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isActive",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "location",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "owner",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "producerKey",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "url",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "votesNum",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "votesWeight",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "RamKind",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "BUY",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SELL",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "RamPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "DateTime",
                                "kind": "SCALAR"
                            },
                            "name": "completedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "eosAmount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "RamKind",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "ramAmount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "RamStatus",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "status",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "tradeFee",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "txid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "userInputSellingRam",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "RamPricePayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "price",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "timestamp",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "RamStatus",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "CONFIRMED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FAILED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "UNCONFIRMED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "RamStatusPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "buyingEos",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "sellingRam",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "SetTgIdAndGetInviteLinksPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "links",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "SsoPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "response",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "StakeAndVoteHistoryPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "HistoryAction",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "action",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "amount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "HistoryStatus",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "status",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "timestamp",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "String",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `String` scalar type represents textual data, represented as UTF-8character sequences. The String type is most often used by GraphQL torepresent free-form human-readable text."
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "TgGroup",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "TgIdPayload",
                                "kind": "OBJECT"
                            },
                            "name": "tgId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "TgIdPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "VipGroup",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "CriterionPayload",
                                "kind": "OBJECT"
                            },
                            "name": "criterion",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "SsoPayload",
                                "kind": "OBJECT"
                            },
                            "name": "sso",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "request",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "arena",
                    "possibleTypes": null,
                    "name": "VotePayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "voted",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "voting",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__EnumValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Type",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__EnumValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "enumValues",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Field",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "fields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "inputFields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "interfaces",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "ofType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "possibleTypes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents scalars, interfaces, object types, unions, enums in the system"
                },
                {
                    "possibleTypes": null,
                    "name": "__DirectiveLocation",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "FIELD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_SPREAD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INLINE_FRAGMENT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MUTATION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "QUERY",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SUBSCRIPTION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__InputValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "defaultValue",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Directive",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__DirectiveLocation",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "locations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onField",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FIELD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onFragment",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FRAGMENT_SPREAD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onOperation",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value OPERATION",
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a directive"
                },
                {
                    "possibleTypes": null,
                    "name": "__Field",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Schema",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Directive",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "directives",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "mutationType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "queryType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "subscriptionType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "types",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a schema"
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "AddWithdrawalInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "memo",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "note",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "targetAddress",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "AddWithdrawalPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "WithdrawalEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "edge",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "Address",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "chain",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customerId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "memo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "value",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Boolean",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Boolean` scalar type represents `true` or `false`."
                },
                {
                    "possibleTypes": null,
                    "name": "DateTime",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `DateTime` scalar type represents a date and time in the UTCtimezone. The DateTime appears in a JSON response as an ISO8601 formattedstring, including UTC timezone (). The parsed date and time string willbe converted to UTC and any UTC offset other than 0 will be rejected."
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "Decimal",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Decimal` scalar type represents signed double-precision fractionalvalues parsed by the `Decimal` library.  The Decimal appears in a JSONresponse as a string to preserve precision."
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "Deposit",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "DateTime",
                                "kind": "SCALAR"
                            },
                            "name": "confirmedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "confirms",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customerId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "explorerUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isInternal",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "note",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DepositState",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "state",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "txid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "DepositConnection",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DepositEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "edges",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Deposit",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "nodes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "PageInfo",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "pageInfo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "DepositEdge",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "cursor",
                            "isDeprecated": false,
                            "description": "A cursor for use in pagination",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Deposit",
                                "kind": "OBJECT"
                            },
                            "name": "node",
                            "isDeprecated": false,
                            "description": "The item at the end of the edge",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "DepositKind",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "AIRDROP",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "BIG_HOLDER_DIVIDEND",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "DEFAULT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "EOSC_TO_EOS",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "EQUALLY_AIRDROP",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "ONE_HOLDER_DIVIDEND",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "REFERRAL_MINING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SINGLE_CUSTOMER",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SNAPSHOTTED_AIRDROP",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "TRADE_MINING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "DepositOrder",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OrderDirection",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "direction",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DepositOrderField",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "field",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "DepositOrderField",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ID",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INSERTED_AT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "DepositState",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "CANCELLED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "CONFIRMED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "PENDING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "WITHHOLD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Int",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Int` scalar type represents non-fractional signed whole numeric values.Int can represent values between `-(2^53 - 1)` and `2^53 - 1` since it isrepresented in JSON as double-precision floating point numbers specifiedby [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point)."
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "OrderDirection",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ASC",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "DESC",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "PageInfo",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "endCursor",
                            "isDeprecated": false,
                            "description": "When paginating forwards, the cursor to continue.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hasNextPage",
                            "isDeprecated": false,
                            "description": "When paginating forwards, are there more items?",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hasPreviousPage",
                            "isDeprecated": false,
                            "description": "When paginating backwards, are there more items?",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "startCursor",
                            "isDeprecated": false,
                            "description": "When paginating backwards, the cursor to continue.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "String",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `String` scalar type represents textual data, represented as UTF-8character sequences. The String type is most often used by GraphQL torepresent free-form human-readable text."
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "Withdrawal",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "DateTime",
                                "kind": "SCALAR"
                            },
                            "name": "completedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customerId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "explain",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "explorerUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "fee",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "feeAssetUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isInternal",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "note",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "recipientId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "WithdrawalState",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "state",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "targetAddress",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "txid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "WithdrawalConnection",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "WithdrawalEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "edges",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Withdrawal",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "nodes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "PageInfo",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "pageInfo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "WithdrawalEdge",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "cursor",
                            "isDeprecated": false,
                            "description": "A cursor for use in pagination",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Withdrawal",
                                "kind": "OBJECT"
                            },
                            "name": "node",
                            "isDeprecated": false,
                            "description": "The item at the end of the edge",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "WithdrawalOrder",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OrderDirection",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "direction",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "WithdrawalOrderField",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "field",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "WithdrawalOrderField",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ID",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INSERTED_AT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "counter",
                    "possibleTypes": null,
                    "name": "WithdrawalState",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "COMPLETED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FAILED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "PENDING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "TRANSACTION_CREATED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__EnumValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__InputValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "defaultValue",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__DirectiveLocation",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "FIELD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_SPREAD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INLINE_FRAGMENT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MUTATION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "QUERY",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SUBSCRIPTION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Type",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__EnumValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "enumValues",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Field",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "fields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "inputFields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "interfaces",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "ofType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "possibleTypes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents scalars, interfaces, object types, unions, enums in the system"
                },
                {
                    "possibleTypes": null,
                    "name": "__Directive",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__DirectiveLocation",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "locations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onField",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FIELD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onFragment",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FRAGMENT_SPREAD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onOperation",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value OPERATION",
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a directive"
                },
                {
                    "possibleTypes": null,
                    "name": "__Schema",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Directive",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "directives",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "mutationType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "queryType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "subscriptionType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "types",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a schema"
                },
                {
                    "possibleTypes": null,
                    "name": "__Field",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Boolean",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Represents `true` or `false` values."
                },
                {
                    "possibleTypes": null,
                    "name": "String",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Represents textual data as UTF-8 character sequences. This type is most often used by GraphQL to represent free-form human-readable text."
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneDailyStatistic",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "Float",
                                "kind": "SCALAR"
                            },
                            "name": "oneAvgPrice",
                            "isDeprecated": false,
                            "description": "ONE \u5e73\u5747\u4ef7\u683c (BTC)",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Float",
                                "kind": "SCALAR"
                            },
                            "name": "oneSnapshot24Avg",
                            "isDeprecated": false,
                            "description": "\u5168\u5e73\u53f0\u5404\u8d26\u6237\u6301\u6709 ONE \u5e73\u5747\u503c\u7684\u603b\u548c (ONE)",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "revenue100wBtc",
                            "isDeprecated": false,
                            "description": "\u8fde\u7eed\u6301\u6709 100\u4e07 ONE \u9884\u8ba1\u8fd4\u5229\u6298\u5408\uff08BTC)",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Date",
                                "kind": "SCALAR"
                            },
                            "name": "statisticalDate",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "totalFeeBtc",
                            "isDeprecated": false,
                            "description": "\u603b\u624b\u7eed\u8d39\u6298\u5408 (BTC)",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "unfrozenOne",
                            "isDeprecated": false,
                            "description": "ONE \u7d2f\u8ba1\u89e3\u51bb (ONE)",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "Date",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Float",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Represents signed double-precision fractional values as specified by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point)."
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneTenMinutelyStatistic",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "inviteMineOne",
                            "isDeprecated": false,
                            "description": "\u9080\u8bf7\u65b0\u7528\u6237\u6316\u77ff\uff08ONE\uff09",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "statTime",
                            "isDeprecated": false,
                            "description": "\u7edf\u8ba1\u65f6\u95f4",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "totalFeeBtc",
                            "isDeprecated": false,
                            "description": "\u6316\u77ff\u533a\u4eca\u65e5\u624b\u7eed\u8d39\uff08BTC\uff09",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "tradeMineOne",
                            "isDeprecated": false,
                            "description": "\u4ea4\u6613\u6316\u77ff\uff08ONE\uff09",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneHourlyStatistic",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "feeBtc",
                            "isDeprecated": false,
                            "description": "\u6316\u77ff\u533a\u624b\u7eed\u8d39\u6298\u5408\uff08BTC\uff09",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "inviteMineOne",
                            "isDeprecated": false,
                            "description": "\u9080\u8bf7\u65b0\u7528\u6237\u6316\u77ff\uff08ONE\uff09",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isDaily",
                            "isDeprecated": false,
                            "description": "\u662f\u5426\u662f\u5386\u53f2\u4e0a\u7684\u6bcf\u65e5\u7edf\u8ba1\u6570\u636e",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "oneAvgPriceBtc",
                            "isDeprecated": false,
                            "description": "\u672c\u5c0f\u65f6 ONE \u5747\u4ef7\uff08BTC\uff09",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "statTime",
                            "isDeprecated": false,
                            "description": "\u7edf\u8ba1\u65f6\u95f4",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "totalUnlockedOne",
                            "isDeprecated": false,
                            "description": "\u5f53\u524d\u6d41\u901a\u603b\u91cf (ONE) ",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "tradeMineOne",
                            "isDeprecated": false,
                            "description": "\u4ea4\u6613\u6316\u77ff\uff08ONE\uff09",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneAssetDailyStatistic",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "isDeprecated": false,
                            "description": "asset UUID",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Date",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "statisticalDate",
                            "isDeprecated": false,
                            "description": "\u65e5\u671f",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "totalDividend",
                            "isDeprecated": false,
                            "description": "\u8fd4\u5229\u6570\u91cf",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "totalTradeFee",
                            "isDeprecated": false,
                            "description": "\u5e73\u53f0\u603b\u624b\u7eed\u8d39",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneHourlyStatisticList",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OneHourlyStatisticConnection",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "oneHourlyStatistic",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "first",
                                    "description": "Returns the first _n_ elements from the list.",
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "after",
                                    "description": "Returns the elements in the list that come after the specified cursor.",
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "last",
                                    "description": "Returns the last _n_ elements from the list.",
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "before",
                                    "description": "Returns the elements in the list that come before the specified cursor.",
                                    "defaultValue": null
                                }
                            ]
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneHourlyStatisticConnection",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OneHourlyStatisticEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "edges",
                            "isDeprecated": false,
                            "description": "A list of edges.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "PageInfo",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "pageInfo",
                            "isDeprecated": false,
                            "description": "Information to aid in pagination.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "The connection type for OneHourlyStatistic."
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneHourlyStatisticEdge",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "cursor",
                            "isDeprecated": false,
                            "description": "A cursor for use in pagination.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OneHourlyStatistic",
                                "kind": "OBJECT"
                            },
                            "name": "node",
                            "isDeprecated": false,
                            "description": "The item at the end of the edge.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "An edge in a connection."
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "PageInfo",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "endCursor",
                            "isDeprecated": false,
                            "description": "When paginating forwards, the cursor to continue.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hasNextPage",
                            "isDeprecated": false,
                            "description": "When paginating forwards, are there more items?",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hasPreviousPage",
                            "isDeprecated": false,
                            "description": "When paginating backwards, are there more items?",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "startCursor",
                            "isDeprecated": false,
                            "description": "When paginating backwards, the cursor to continue.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Information about pagination in a connection."
                },
                {
                    "possibleTypes": null,
                    "name": "Int",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1."
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneDailyStatisticList",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OneDailyStatisticConnection",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "oneDailyStatistic",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "first",
                                    "description": "Returns the first _n_ elements from the list.",
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "after",
                                    "description": "Returns the elements in the list that come after the specified cursor.",
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "last",
                                    "description": "Returns the last _n_ elements from the list.",
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "before",
                                    "description": "Returns the elements in the list that come before the specified cursor.",
                                    "defaultValue": null
                                }
                            ]
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneDailyStatisticConnection",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OneDailyStatisticEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "edges",
                            "isDeprecated": false,
                            "description": "A list of edges.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "PageInfo",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "pageInfo",
                            "isDeprecated": false,
                            "description": "Information to aid in pagination.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "The connection type for OneDailyStatistic."
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "OneDailyStatisticEdge",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "cursor",
                            "isDeprecated": false,
                            "description": "A cursor for use in pagination.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OneDailyStatistic",
                                "kind": "OBJECT"
                            },
                            "name": "node",
                            "isDeprecated": false,
                            "description": "The item at the end of the edge.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "An edge in a connection."
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "MineConfig",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "appliedTime",
                            "isDeprecated": false,
                            "description": "\u914d\u7f6e\u5f00\u59cb\u751f\u6548\u7684\u65f6\u95f4",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "confKey",
                            "isDeprecated": false,
                            "description": "Config key",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Float",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "confValue",
                            "isDeprecated": false,
                            "description": "Config value",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "DateTime",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Schema",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__Directive",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "directives",
                            "isDeprecated": false,
                            "description": "A list of all directives supported by this server.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "mutationType",
                            "isDeprecated": false,
                            "description": "If this server supports mutation, the type that mutation operations will be rooted at.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "queryType",
                            "isDeprecated": false,
                            "description": "The type that query operations will be rooted at.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "subscriptionType",
                            "isDeprecated": false,
                            "description": "If this server support subscription, the type that subscription operations will be rooted at.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__Type",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "types",
                            "isDeprecated": false,
                            "description": "A list of all types supported by this server.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "A GraphQL Schema defines the capabilities of a GraphQL server. It exposes all available types and directives on the server, as well as the entry points for query, mutation, and subscription operations."
                },
                {
                    "possibleTypes": null,
                    "name": "__Type",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__EnumValue",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "enumValues",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__Field",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "fields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__InputValue",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "inputFields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__Type",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "interfaces",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__TypeKind",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "ofType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__Type",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "possibleTypes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "The fundamental unit of any GraphQL Schema is the type. There are many kinds of types in GraphQL as represented by the `__TypeKind` enum.Depending on the kind of a type, certain fields describe information about that type. Scalar types provide no information beyond a name and description, while Enum types provide their values. Object and Interface types provide the fields they describe. Abstract types, Union and Interface, provide the Object types possible at runtime. List and NonNull types compose other types."
                },
                {
                    "possibleTypes": null,
                    "name": "__Field",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__InputValue",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type."
                },
                {
                    "possibleTypes": null,
                    "name": "__Directive",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__InputValue",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__DirectiveLocation",
                                            "kind": "ENUM"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "locations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "onField",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Use `locations`.",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "onFragment",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Use `locations`.",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "onOperation",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Use `locations`.",
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.In some cases, you need to provide options to alter GraphQL's execution behavior in ways field arguments will not suffice, such as conditionally including or skipping a field. Directives provide this by describing additional information to the executor."
                },
                {
                    "possibleTypes": null,
                    "name": "__EnumValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "One possible value for a given Enum. Enum values are unique values, not a placeholder for a string or numeric value. However an Enum value is returned in a JSON response as a string."
                },
                {
                    "possibleTypes": null,
                    "name": "__InputValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "defaultValue",
                            "isDeprecated": false,
                            "description": "A GraphQL-formatted string representing the default value for this input value.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value."
                },
                {
                    "service": "data-market",
                    "possibleTypes": null,
                    "name": "__TypeKind",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "SCALAR",
                            "isDeprecated": false,
                            "description": "Indicates this type is a scalar.",
                            "deprecationReason": null
                        },
                        {
                            "name": "OBJECT",
                            "isDeprecated": false,
                            "description": "Indicates this type is an object. `fields` and `interfaces` are valid fields.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INTERFACE",
                            "isDeprecated": false,
                            "description": "Indicates this type is an interface. `fields` and `possibleTypes` are valid fields.",
                            "deprecationReason": null
                        },
                        {
                            "name": "UNION",
                            "isDeprecated": false,
                            "description": "Indicates this type is a union. `possibleTypes` is a valid field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "ENUM",
                            "isDeprecated": false,
                            "description": "Indicates this type is an enum. `enumValues` is a valid field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INPUT_OBJECT",
                            "isDeprecated": false,
                            "description": "Indicates this type is an input object. `inputFields` is a valid field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "LIST",
                            "isDeprecated": false,
                            "description": "Indicates this type is a list. `ofType` is a valid field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "NON_NULL",
                            "isDeprecated": false,
                            "description": "Indicates this type is a non-null. `ofType` is a valid field.",
                            "deprecationReason": null
                        }
                    ],
                    "description": "An enum describing what kind of type a given `__Type` is."
                },
                {
                    "possibleTypes": null,
                    "name": "__DirectiveLocation",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "QUERY",
                            "isDeprecated": false,
                            "description": "Location adjacent to a query operation.",
                            "deprecationReason": null
                        },
                        {
                            "name": "MUTATION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a mutation operation.",
                            "deprecationReason": null
                        },
                        {
                            "name": "SUBSCRIPTION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a subscription operation.",
                            "deprecationReason": null
                        },
                        {
                            "name": "FIELD",
                            "isDeprecated": false,
                            "description": "Location adjacent to a field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a fragment definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_SPREAD",
                            "isDeprecated": false,
                            "description": "Location adjacent to a fragment spread.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INLINE_FRAGMENT",
                            "isDeprecated": false,
                            "description": "Location adjacent to an inline fragment.",
                            "deprecationReason": null
                        },
                        {
                            "name": "SCHEMA",
                            "isDeprecated": false,
                            "description": "Location adjacent to a schema definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "SCALAR",
                            "isDeprecated": false,
                            "description": "Location adjacent to a scalar definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "OBJECT",
                            "isDeprecated": false,
                            "description": "Location adjacent to an object type definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "FIELD_DEFINITION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a field definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "ARGUMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": "Location adjacent to an argument definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INTERFACE",
                            "isDeprecated": false,
                            "description": "Location adjacent to an interface definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "UNION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a union definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "ENUM",
                            "isDeprecated": false,
                            "description": "Location adjacent to an enum definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "ENUM_VALUE",
                            "isDeprecated": false,
                            "description": "Location adjacent to an enum value definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INPUT_OBJECT",
                            "isDeprecated": false,
                            "description": "Location adjacent to an input object type definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INPUT_FIELD_DEFINITION",
                            "isDeprecated": false,
                            "description": "Location adjacent to an input object field definition.",
                            "deprecationReason": null
                        }
                    ],
                    "description": "A Directive can be adjacent to many parts of the GraphQL language, a __DirectiveLocation describes one such possible adjacencies."
                },
                {
                    "possibleTypes": null,
                    "name": "Boolean",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Represents `true` or `false` values."
                },
                {
                    "possibleTypes": null,
                    "name": "String",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Represents textual data as UTF-8 character sequences. This type is most often used by GraphQL to represent free-form human-readable text."
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "Document",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "content",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Time",
                                "kind": "SCALAR"
                            },
                            "name": "createdAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "customerId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Time",
                                "kind": "SCALAR"
                            },
                            "name": "docExpireAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "docType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ID",
                                "kind": "SCALAR"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "nation",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "number",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Time",
                                "kind": "SCALAR"
                            },
                            "name": "statusExpireAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Time",
                                "kind": "SCALAR"
                            },
                            "name": "updatedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "ID",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Represents a unique identifier that is Base64 obfuscated. It is often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as ``) or integer (such as `4`) input value will be accepted as an ID."
                },
                {
                    "possibleTypes": null,
                    "name": "Int",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1."
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "Time",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "Time"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "Image",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "ID",
                                "kind": "SCALAR"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "signUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycRequest",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "brokerId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Time",
                                "kind": "SCALAR"
                            },
                            "name": "createdAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "customerId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "docId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ID",
                                "kind": "SCALAR"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "provider",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "requestId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "status",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Time",
                                "kind": "SCALAR"
                            },
                            "name": "updatedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Int",
                                "kind": "SCALAR"
                            },
                            "name": "userId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "UploadDocumentPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Image",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "image",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of UploadDocument"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "UploadDocumentInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "type",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "desc",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Upload",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "file",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of UploadDocument"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "Upload",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "ManualDocumentVerificationPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of ManualDocumentVerification"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "ManualDocumentVerificationInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "customer_id",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "doc_id",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "KycStatus",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kyc_status",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "reason",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of ManualDocumentVerification"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycStatus",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ACCEPTED",
                            "isDeprecated": false,
                            "description": "accepted",
                            "deprecationReason": null
                        },
                        {
                            "name": "REJECTED",
                            "isDeprecated": false,
                            "description": "rejected",
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "CreateDocumentVerificationPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "KycRequest",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kyc_request",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of CreateDocumentVerification"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "CreateDocumentVerificationInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "nation",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "doc_type",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "parameters",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of CreateDocumentVerification"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycStartRequestPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "KycRequest",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kycRequest",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycStartRequest"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycStartRequestInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycStartRequest"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUpdateNamePayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycUpdateName"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUpdateNameInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requestId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycUpdateName"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUpdateNationPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycUpdateNation"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUpdateNationInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requestId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "nation",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycUpdateNation"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUpdateDocPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycUpdateDoc"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUpdateDocInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requestId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "docType",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycUpdateDoc"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUpdateNumberPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycUpdateNumber"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUpdateNumberInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requestId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "number",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycUpdateNumber"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUploadFrontImagePayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycUploadFrontImage"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUploadFrontImageInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requestId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Upload",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "file",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycUploadFrontImage"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUploadBackImagePayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycUploadBackImage"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUploadBackImageInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requestId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Upload",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "file",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycUploadBackImage"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUploadPortraitImagePayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycUploadPortraitImage"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycUploadPortraitImageInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requestId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Upload",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "file",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycUploadPortraitImage"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycSubmitRequestPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": "A unique identifier for the client performing the mutation.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "result",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Autogenerated return type of KycSubmitRequest"
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "KycSubmitRequestInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "requestId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": "A unique identifier for the client performing the mutation.",
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": "Autogenerated input type of KycSubmitRequest"
                },
                {
                    "possibleTypes": null,
                    "name": "__Schema",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__Directive",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "directives",
                            "isDeprecated": false,
                            "description": "A list of all directives supported by this server.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "mutationType",
                            "isDeprecated": false,
                            "description": "If this server supports mutation, the type that mutation operations will be rooted at.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "queryType",
                            "isDeprecated": false,
                            "description": "The type that query operations will be rooted at.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "subscriptionType",
                            "isDeprecated": false,
                            "description": "If this server support subscription, the type that subscription operations will be rooted at.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__Type",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "types",
                            "isDeprecated": false,
                            "description": "A list of all types supported by this server.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "A GraphQL Schema defines the capabilities of a GraphQL server. It exposes all available types and directives on the server, as well as the entry points for query, mutation, and subscription operations."
                },
                {
                    "possibleTypes": null,
                    "name": "__Type",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__EnumValue",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "enumValues",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__Field",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "fields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__InputValue",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "inputFields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__Type",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "interfaces",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__TypeKind",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "ofType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "__Type",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "possibleTypes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "The fundamental unit of any GraphQL Schema is the type. There are many kinds of types in GraphQL as represented by the `__TypeKind` enum.Depending on the kind of a type, certain fields describe information about that type. Scalar types provide no information beyond a name and description, while Enum types provide their values. Object and Interface types provide the fields they describe. Abstract types, Union and Interface, provide the Object types possible at runtime. List and NonNull types compose other types."
                },
                {
                    "possibleTypes": null,
                    "name": "__Field",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__InputValue",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type."
                },
                {
                    "possibleTypes": null,
                    "name": "__Directive",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__InputValue",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "__DirectiveLocation",
                                            "kind": "ENUM"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "locations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "onField",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Use `locations`.",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "onFragment",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Use `locations`.",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "onOperation",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Use `locations`.",
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.In some cases, you need to provide options to alter GraphQL's execution behavior in ways field arguments will not suffice, such as conditionally including or skipping a field. Directives provide this by describing additional information to the executor."
                },
                {
                    "possibleTypes": null,
                    "name": "__EnumValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "One possible value for a given Enum. Enum values are unique values, not a placeholder for a string or numeric value. However an Enum value is returned in a JSON response as a string."
                },
                {
                    "possibleTypes": null,
                    "name": "__InputValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "defaultValue",
                            "isDeprecated": false,
                            "description": "A GraphQL-formatted string representing the default value for this input value.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value."
                },
                {
                    "service": "kyc",
                    "possibleTypes": null,
                    "name": "__TypeKind",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "SCALAR",
                            "isDeprecated": false,
                            "description": "Indicates this type is a scalar.",
                            "deprecationReason": null
                        },
                        {
                            "name": "OBJECT",
                            "isDeprecated": false,
                            "description": "Indicates this type is an object. `fields` and `interfaces` are valid fields.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INTERFACE",
                            "isDeprecated": false,
                            "description": "Indicates this type is an interface. `fields` and `possibleTypes` are valid fields.",
                            "deprecationReason": null
                        },
                        {
                            "name": "UNION",
                            "isDeprecated": false,
                            "description": "Indicates this type is a union. `possibleTypes` is a valid field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "ENUM",
                            "isDeprecated": false,
                            "description": "Indicates this type is an enum. `enumValues` is a valid field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INPUT_OBJECT",
                            "isDeprecated": false,
                            "description": "Indicates this type is an input object. `inputFields` is a valid field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "LIST",
                            "isDeprecated": false,
                            "description": "Indicates this type is a list. `ofType` is a valid field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "NON_NULL",
                            "isDeprecated": false,
                            "description": "Indicates this type is a non-null. `ofType` is a valid field.",
                            "deprecationReason": null
                        }
                    ],
                    "description": "An enum describing what kind of type a given `__Type` is."
                },
                {
                    "possibleTypes": null,
                    "name": "__DirectiveLocation",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "QUERY",
                            "isDeprecated": false,
                            "description": "Location adjacent to a query operation.",
                            "deprecationReason": null
                        },
                        {
                            "name": "MUTATION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a mutation operation.",
                            "deprecationReason": null
                        },
                        {
                            "name": "SUBSCRIPTION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a subscription operation.",
                            "deprecationReason": null
                        },
                        {
                            "name": "FIELD",
                            "isDeprecated": false,
                            "description": "Location adjacent to a field.",
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a fragment definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_SPREAD",
                            "isDeprecated": false,
                            "description": "Location adjacent to a fragment spread.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INLINE_FRAGMENT",
                            "isDeprecated": false,
                            "description": "Location adjacent to an inline fragment.",
                            "deprecationReason": null
                        },
                        {
                            "name": "SCHEMA",
                            "isDeprecated": false,
                            "description": "Location adjacent to a schema definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "SCALAR",
                            "isDeprecated": false,
                            "description": "Location adjacent to a scalar definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "OBJECT",
                            "isDeprecated": false,
                            "description": "Location adjacent to an object type definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "FIELD_DEFINITION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a field definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "ARGUMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": "Location adjacent to an argument definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INTERFACE",
                            "isDeprecated": false,
                            "description": "Location adjacent to an interface definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "UNION",
                            "isDeprecated": false,
                            "description": "Location adjacent to a union definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "ENUM",
                            "isDeprecated": false,
                            "description": "Location adjacent to an enum definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "ENUM_VALUE",
                            "isDeprecated": false,
                            "description": "Location adjacent to an enum value definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INPUT_OBJECT",
                            "isDeprecated": false,
                            "description": "Location adjacent to an input object type definition.",
                            "deprecationReason": null
                        },
                        {
                            "name": "INPUT_FIELD_DEFINITION",
                            "isDeprecated": false,
                            "description": "Location adjacent to an input object field definition.",
                            "deprecationReason": null
                        }
                    ],
                    "description": "A Directive can be adjacent to many parts of the GraphQL language, a __DirectiveLocation describes one such possible adjacencies."
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "Account",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "assetUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "balance",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "lockedBalance",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "AddOrderInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "price",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OrderSide",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "side",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "AddOrderPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Order",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "order",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "Bar",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "close",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "high",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "low",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "open",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "BarPeriod",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "period",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "time",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "volume",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "BarOrder",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ASC",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "DESC",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "BarPeriod",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "DAY1",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "HOUR1",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "HOUR12",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "HOUR3",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "HOUR4",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "HOUR6",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MIN1",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MIN15",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MIN30",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MIN5",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "WEEK1",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Boolean",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Boolean` scalar type represents `true` or `false`."
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "CancelAllOrdersInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "marketUuid",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "CancelAllOrdersPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "Order",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "orders",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "CancelOrderInput",
                    "kind": "INPUT_OBJECT",
                    "interfaces": null,
                    "inputFields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "description": null,
                            "defaultValue": null
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "description": null,
                            "defaultValue": null
                        }
                    ],
                    "fields": null,
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "CancelOrderPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "clientMutationId",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Order",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "order",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "DateTime",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `DateTime` scalar type represents a date and time in the UTCtimezone. The DateTime appears in a JSON response as an ISO8601 formattedstring, including UTC timezone (). The parsed date and time string willbe converted to UTC and any UTC offset other than 0 will be rejected."
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "Decimal",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Decimal` scalar type represents signed double-precision fractionalvalues parsed by the `Decimal` library.  The Decimal appears in a JSONresponse as a string to preserve precision."
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "Depth",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "PriceLevel",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "asks",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "PriceLevel",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "bids",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "ID",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `ID` scalar type represents a unique identifier, often used torefetch an object or as key for a cache. The ID type appears in a JSONresponse as a String; however, it is not intended to be human-readable.When expected as an input type, any string (such as ``) or integer(such as `4`) input value will be accepted as an ID."
                },
                {
                    "possibleTypes": null,
                    "name": "Int",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Int` scalar type represents non-fractional signed whole numeric values.Int can represent values between `-(2^53 - 1)` and `2^53 - 1` since it isrepresented in JSON as double-precision floating point numbers specifiedby [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point)."
                },
                {
                    "possibleTypes": null,
                    "name": "RootMutationType",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "AddApiKeyPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "addApiKey",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "AddApiKeyInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "AddFavouriteMarketPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "addFavouriteMarket",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "AddFavouriteMarketInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "AddQualificationPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "addQualification",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "AddQualificationInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "AddWithdrawalPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "addWithdrawal",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "AddWithdrawalInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "AuthenticateCustomerPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "authenticateCustomer",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "AuthenticateCustomerInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ConfirmEmailPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "confirmEmail",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "ConfirmEmailInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "CreateCustomerPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "createCustomer",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "CreateCustomerInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "CreateSessionPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "createSession",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "CreateSessionInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "LockAssetPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "lockAsset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "LockAssetInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "RemoveApiKeyPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "removeApiKey",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "RemoveApiKeyInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "RemoveFavouriteMarketPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "removeFavouriteMarket",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "RemoveFavouriteMarketInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ResetAssetPinPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "resetAssetPin",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "ResetAssetPinInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ResetOtpPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "resetOtp",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "ResetOtpInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ResetPasswordPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "resetPassword",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "ResetPasswordInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "SendConfirmationEmailPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "sendConfirmationEmail",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "SendConfirmationEmailInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "SendPasswordResetEmailPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "sendPasswordResetEmail",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "SendPasswordResetEmailInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "UnlockAssetPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "unlockAsset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "UnlockAssetInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "UpdateAssetPinPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "updateAssetPin",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "UpdateAssetPinInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "UpdateOtpPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "updateOtp",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "UpdateOtpInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "UpdatePasswordPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "updatePassword",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "UpdatePasswordInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "UpdateUserPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "updateUser",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "UpdateUserInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "VerifyPasswordPayload",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "verifyPassword",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "VerifyPasswordInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ActionPayload",
                                "kind": "OBJECT"
                            },
                            "service": "arena",
                            "name": "arenaBuyRam",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Decimal",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "amount",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "PollVotePayload",
                                "kind": "OBJECT"
                            },
                            "service": "arena",
                            "name": "arenaPollVote",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "choice",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Int",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "pollId",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ActionPayload",
                                "kind": "OBJECT"
                            },
                            "service": "arena",
                            "name": "arenaSellRam",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Decimal",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "amount",
                                    "description": "user input ram amount (KB)",
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "SetTgIdAndGetInviteLinksPayload",
                                "kind": "OBJECT"
                            },
                            "service": "arena",
                            "name": "arenaSetTgIdAndGetInviteLinks",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "tgId",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ActionPayload",
                                "kind": "OBJECT"
                            },
                            "service": "arena",
                            "name": "arenaStakeOrder",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Int",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "amount",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ActionPayload",
                                "kind": "OBJECT"
                            },
                            "service": "arena",
                            "name": "arenaVoteProducers",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": {
                                                "ofType": null,
                                                "name": "String",
                                                "kind": "SCALAR"
                                            },
                                            "name": null,
                                            "kind": "NON_NULL"
                                        },
                                        "name": null,
                                        "kind": "LIST"
                                    },
                                    "name": "producers",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "AddWithdrawalPayload",
                                "kind": "OBJECT"
                            },
                            "service": "counter",
                            "name": "addWithdrawal",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "AddWithdrawalInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "CreateDocumentVerificationPayload",
                                "kind": "OBJECT"
                            },
                            "service": "kyc",
                            "name": "createDocumentVerification",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "CreateDocumentVerificationInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "KycStartRequestPayload",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "kyc",
                            "name": "kycStartRequest",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycStartRequestInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "KycSubmitRequestPayload",
                                "kind": "OBJECT"
                            },
                            "service": "kyc",
                            "name": "kycSubmitRequest",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycSubmitRequestInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "KycUpdateDocPayload",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "kyc",
                            "name": "kycUpdateDocType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycUpdateDocInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "KycUpdateNamePayload",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "kyc",
                            "name": "kycUpdateName",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycUpdateNameInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "KycUpdateNationPayload",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "kyc",
                            "name": "kycUpdateNation",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycUpdateNationInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "KycUpdateNumberPayload",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "kyc",
                            "name": "kycUpdateNumber",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycUpdateNumberInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "KycUploadBackImagePayload",
                                "kind": "OBJECT"
                            },
                            "service": "kyc",
                            "name": "kycUploadBackImage",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycUploadBackImageInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "KycUploadFrontImagePayload",
                                "kind": "OBJECT"
                            },
                            "service": "kyc",
                            "name": "kycUploadFrontImage",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycUploadFrontImageInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "KycUploadPortraitImagePayload",
                                "kind": "OBJECT"
                            },
                            "service": "kyc",
                            "name": "kycUploadPortraitImage",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "KycUploadPortraitImageInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ManualDocumentVerificationPayload",
                                "kind": "OBJECT"
                            },
                            "service": "kyc",
                            "name": "manualDocumentVerification",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "ManualDocumentVerificationInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "UploadDocumentPayload",
                                "kind": "OBJECT"
                            },
                            "service": "kyc",
                            "name": "uploadDocument",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "UploadDocumentInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "AddOrderPayload",
                                "kind": "OBJECT"
                            },
                            "service": "matcher",
                            "name": "addOrder",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "AddOrderInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "CancelAllOrdersPayload",
                                "kind": "OBJECT"
                            },
                            "service": "matcher",
                            "name": "cancelAllOrders",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "CancelAllOrdersInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "CancelOrderPayload",
                                "kind": "OBJECT"
                            },
                            "service": "matcher",
                            "name": "cancelOrder",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "CancelOrderInput",
                                            "kind": "INPUT_OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "input",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "Order",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "avgDealPrice",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "filledAmount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "price",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OrderSide",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "side",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OrderState",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "state",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "updatedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "OrderConnection",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OrderEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "edges",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Order",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "nodes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "PageInfo",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "pageInfo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "OrderEdge",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "cursor",
                            "isDeprecated": false,
                            "description": "A cursor for use in pagination",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Order",
                                "kind": "OBJECT"
                            },
                            "name": "node",
                            "isDeprecated": false,
                            "description": "The item at the end of the edge",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "OrderSide",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ASK",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "BID",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "OrderState",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "CANCELED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FILLED",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "PENDING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "PageInfo",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "endCursor",
                            "isDeprecated": false,
                            "description": "When paginating forwards, the cursor to continue.",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hasNextPage",
                            "isDeprecated": false,
                            "description": "When paginating forwards, are there more items?",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Boolean",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "hasPreviousPage",
                            "isDeprecated": false,
                            "description": "When paginating backwards, are there more items?",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "startCursor",
                            "isDeprecated": false,
                            "description": "When paginating backwards, the cursor to continue.",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "PriceLevel",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Int",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "orderCount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "price",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "String",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `String` scalar type represents textual data, represented as UTF-8character sequences. The String type is most often used by GraphQL torepresent free-form human-readable text."
                },
                {
                    "possibleTypes": null,
                    "name": "RootSubscriptionType",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "service": "broker",
                            "name": "authenticate",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "token",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Bar",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "matcher",
                            "name": "marketBarsSubscription",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "BarPeriod",
                                            "kind": "ENUM"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "period",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Depth",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "matcher",
                            "name": "marketDepthSubscription",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Ticker",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "matcher",
                            "name": "marketTickersSubscription",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Trade",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "matcher",
                            "name": "marketTradesSubscription",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Account",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "matcher",
                            "name": "myAccountsSubscription",
                            "isDeprecated": false,
                            "description": "needs authentication",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Order",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "matcher",
                            "name": "myOrdersSubscription",
                            "isDeprecated": false,
                            "description": "needs authentication",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "Ticker",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "PriceLevel",
                                "kind": "OBJECT"
                            },
                            "name": "ask",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "PriceLevel",
                                "kind": "OBJECT"
                            },
                            "name": "bid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "close",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "createdAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "dailyChange",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "dailyChangePerc",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "high",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "low",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "open",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "volume",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "Trade",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "amount",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "id",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "DateTime",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "insertedAt",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "ID",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "marketUuid",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Decimal",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "price",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OrderSide",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "takerSide",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "ViewerSide",
                                "kind": "ENUM"
                            },
                            "name": "viewerSide",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "TradeConnection",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "TradeEdge",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "edges",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Trade",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "nodes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "PageInfo",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "pageInfo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "TradeEdge",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "cursor",
                            "isDeprecated": false,
                            "description": "A cursor for use in pagination",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Trade",
                                "kind": "OBJECT"
                            },
                            "name": "node",
                            "isDeprecated": false,
                            "description": "The item at the end of the edge",
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "matcher",
                    "possibleTypes": null,
                    "name": "ViewerSide",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "ASK",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "BID",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SELF_TRADING",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__DirectiveLocation",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "FIELD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_SPREAD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INLINE_FRAGMENT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MUTATION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "QUERY",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SUBSCRIPTION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Directive",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__DirectiveLocation",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "locations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onField",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FIELD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onFragment",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FRAGMENT_SPREAD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onOperation",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value OPERATION",
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a directive"
                },
                {
                    "possibleTypes": null,
                    "name": "__Schema",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Directive",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "directives",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "mutationType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "queryType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "subscriptionType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "types",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a schema"
                },
                {
                    "possibleTypes": null,
                    "name": "__Field",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__EnumValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Type",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__EnumValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "enumValues",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Field",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "fields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "inputFields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "interfaces",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "ofType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "possibleTypes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents scalars, interfaces, object types, unions, enums in the system"
                },
                {
                    "possibleTypes": null,
                    "name": "__InputValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "defaultValue",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "prezzo",
                    "possibleTypes": null,
                    "name": "AssetPricesPayload",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "String",
                                    "kind": "SCALAR"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "name": "baseAsset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Decimal",
                                "kind": "SCALAR"
                            },
                            "name": "price",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "Boolean",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Boolean` scalar type represents `true` or `false`."
                },
                {
                    "service": "prezzo",
                    "possibleTypes": null,
                    "name": "Decimal",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Decimal` scalar type represents signed double-precision fractionalvalues parsed by the `Decimal` library.  The Decimal appears in a JSONresponse as a string to preserve precision."
                },
                {
                    "possibleTypes": null,
                    "name": "String",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `String` scalar type represents textual data, represented as UTF-8character sequences. The String type is most often used by GraphQL torepresent free-form human-readable text."
                },
                {
                    "possibleTypes": null,
                    "name": "__Directive",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__DirectiveLocation",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "locations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onField",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FIELD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onFragment",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FRAGMENT_SPREAD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onOperation",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value OPERATION",
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a directive"
                },
                {
                    "possibleTypes": null,
                    "name": "__DirectiveLocation",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "FIELD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_SPREAD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INLINE_FRAGMENT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MUTATION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "QUERY",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SUBSCRIPTION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__EnumValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Field",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__InputValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "defaultValue",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Schema",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Directive",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "directives",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "mutationType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "queryType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "subscriptionType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "types",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a schema"
                },
                {
                    "possibleTypes": null,
                    "name": "__Type",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__EnumValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "enumValues",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Field",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "fields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "inputFields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "interfaces",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "ofType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "possibleTypes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents scalars, interfaces, object types, unions, enums in the system"
                },
                {
                    "possibleTypes": null,
                    "name": "Boolean",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `Boolean` scalar type represents `true` or `false`."
                },
                {
                    "possibleTypes": null,
                    "name": "RootQueryType",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Address",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "broker",
                            "name": "addresses",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Use viewer.addresses instead",
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "assetUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Asset",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "asset",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "uuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "Asset",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "broker",
                            "name": "assets",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Invitee",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "broker",
                            "name": "invitees",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Market",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "market",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "uuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "Market",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "broker",
                            "name": "markets",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Metadata",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "broker",
                            "name": "meta",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OperationEvent",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "operation",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OtpSecret",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "otpSecret",
                            "isDeprecated": false,
                            "description": "get OTP secret",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Session",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "refreshSession",
                            "isDeprecated": false,
                            "description": "Refresh auth token",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "TradeConnection",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "trades",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "after",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "before",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "first",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "last",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Customer",
                                "kind": "OBJECT"
                            },
                            "service": "broker",
                            "name": "viewer",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "PollInfoPayload",
                                "kind": "OBJECT"
                            },
                            "service": "arena",
                            "name": "arenaPollInfo",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Int",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "pollId",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "ProducerAdPayload",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "arena",
                            "name": "arenaProducerAds",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "ProducerPayload",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "arena",
                            "name": "arenaProducers",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "RamPayload",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "arena",
                            "name": "arenaRamList",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "RamPricePayload",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "arena",
                            "name": "arenaRamPrice",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "RamStatusPayload",
                                "kind": "OBJECT"
                            },
                            "service": "arena",
                            "name": "arenaRamStatus",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "StakeAndVoteHistoryPayload",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "arena",
                            "name": "arenaStakeAndVoteHistory",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "AmountPayload",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "arena",
                            "name": "arenaStakeStatus",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "VotePayload",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "arena",
                            "name": "arenaVoteStatus",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Campaigns",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "arena",
                            "name": "campaigns",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Address",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "counter",
                            "name": "addresses",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "assetUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "DepositConnection",
                                "kind": "OBJECT"
                            },
                            "service": "counter",
                            "name": "deposits",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "after",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "afterTime",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "assetUuid",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "before",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "beforeTime",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "first",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "DepositKind",
                                            "kind": "ENUM"
                                        },
                                        "name": null,
                                        "kind": "LIST"
                                    },
                                    "name": "kinds",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "last",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DepositOrder",
                                        "kind": "INPUT_OBJECT"
                                    },
                                    "name": "orderBy",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "WithdrawalConnection",
                                "kind": "OBJECT"
                            },
                            "service": "counter",
                            "name": "withdrawals",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "after",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "afterTime",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "assetUuid",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "before",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "beforeTime",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "first",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "last",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "WithdrawalOrder",
                                        "kind": "INPUT_OBJECT"
                                    },
                                    "name": "orderBy",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "MineConfig",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "data-market",
                            "name": "mineConfigs",
                            "isDeprecated": false,
                            "description": "\u6839\u636e Key \u83b7\u53d6\u6316\u77ff\u76f8\u5173\u7684\u914d\u7f6e",
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": {
                                                "ofType": {
                                                    "name": "String",
                                                    "kind": "SCALAR"
                                                },
                                                "name": null,
                                                "kind": "NON_NULL"
                                            },
                                            "name": null,
                                            "kind": "LIST"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "confKeys",
                                    "description": "\u9700\u8981\u83b7\u53d6\u7684 Key \u5217\u8868[rebate_ratio: \u9080\u8bf7\u8fd4\u5229\u7cfb\u6570]",
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "appliedTime",
                                    "description": "\u751f\u6548\u65f6\u95f4",
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": {
                                            "name": "OneAssetDailyStatistic",
                                            "kind": "OBJECT"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": null,
                                    "kind": "LIST"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "data-market",
                            "name": "oneAssetDailyStatistics",
                            "isDeprecated": false,
                            "description": "\u7ed9\u5b9a\u65e5\u671f ONE \u5206\u5e01\u79cd\u7edf\u8ba1",
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Date",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "date",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OneDailyStatisticList",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "data-market",
                            "name": "oneDailyStatisticHistory",
                            "isDeprecated": false,
                            "description": "\u6bcf\u5c0f\u65f6\u4ea4\u6613\u624b\u7eed\u8d39\u8fd4\u56de",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "OneHourlyStatisticList",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "data-market",
                            "name": "oneHourlyStatisticHistory",
                            "isDeprecated": false,
                            "description": "\u6bcf\u5c0f\u65f6\u4ea4\u6613\u624b\u7eed\u8d39\u8fd4\u56de",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OneDailyStatistic",
                                "kind": "OBJECT"
                            },
                            "service": "data-market",
                            "name": "oneLatestDailyStatistic",
                            "isDeprecated": false,
                            "description": "[ONE] \u6700\u65b0\u4e00\u5929\u7684\u7edf\u8ba1",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OneHourlyStatistic",
                                "kind": "OBJECT"
                            },
                            "service": "data-market",
                            "name": "oneLatestHourlyStatistic",
                            "isDeprecated": false,
                            "description": "[ONE] \u6700\u65b0\u6bcf\u5c0f\u65f6\u7edf\u8ba1",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OneTenMinutelyStatistic",
                                "kind": "OBJECT"
                            },
                            "service": "data-market",
                            "name": "oneLatestTenMinutelyStatistic",
                            "isDeprecated": false,
                            "description": "[ONE] \u6700\u65b010\u5206\u949f\u7edf\u8ba1",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "service": "data-market",
                            "name": "oneMineLockedOneThreshold",
                            "isDeprecated": false,
                            "description": "\u4eca\u65e5ONE\u9501\u5b9a\u4e0b\u9650",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Float",
                                "kind": "SCALAR"
                            },
                            "service": "data-market",
                            "name": "oneMiningLimitation",
                            "isDeprecated": false,
                            "description": "\u4eca\u65e5\u6316\u77ff\u4e0a\u9650",
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OneDailyStatistic",
                                "kind": "OBJECT"
                            },
                            "service": "data-market",
                            "name": "oneStatistic",
                            "isDeprecated": false,
                            "description": "\u7ed9\u5b9a\u65e5\u671f\u7684 ONE \u6bcf\u65e5\u7edf\u8ba1\u4fe1\u606f",
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Date",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "date",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Image",
                                "kind": "OBJECT"
                            },
                            "service": "kyc",
                            "name": "generateImageUrl",
                            "isDeprecated": false,
                            "description": "",
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Int",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "img_id",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "KycRequest",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "kyc",
                            "name": "retrieveKycRequests",
                            "isDeprecated": false,
                            "description": "",
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "status",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Time",
                                        "kind": "SCALAR"
                                    },
                                    "name": "start_date",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Time",
                                        "kind": "SCALAR"
                                    },
                                    "name": "end_date",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "Document",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "kyc",
                            "name": "retrieveVerificationDocument",
                            "isDeprecated": false,
                            "description": "retrieve verification document",
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "Int",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "customer_id",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "Document",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "kyc",
                            "name": "retrieveVerificationDocumentByNumber",
                            "isDeprecated": false,
                            "description": "",
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "number",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "Bar",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "matcher",
                            "name": "bars",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "endTime",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "limit",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "BarOrder",
                                        "kind": "ENUM"
                                    },
                                    "name": "order",
                                    "description": "default to desc",
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "BarPeriod",
                                            "kind": "ENUM"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "period",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "startTime",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Depth",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "matcher",
                            "name": "depth",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "limit",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Decimal",
                                        "kind": "SCALAR"
                                    },
                                    "name": "precision",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "Account",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "matcher",
                            "name": "myAccounts",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": {
                                                "ofType": null,
                                                "name": "String",
                                                "kind": "SCALAR"
                                            },
                                            "name": null,
                                            "kind": "NON_NULL"
                                        },
                                        "name": null,
                                        "kind": "LIST"
                                    },
                                    "name": "assetUuids",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "OrderConnection",
                                "kind": "OBJECT"
                            },
                            "service": "matcher",
                            "name": "myOrders",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "after",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "before",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "first",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "last",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "OrderSide",
                                        "kind": "ENUM"
                                    },
                                    "name": "side",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "OrderState",
                                        "kind": "ENUM"
                                    },
                                    "name": "state",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "TradeConnection",
                                "kind": "OBJECT"
                            },
                            "service": "matcher",
                            "name": "myTrades",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "after",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "afterTime",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "before",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "DateTime",
                                        "kind": "SCALAR"
                                    },
                                    "name": "beforeTime",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "first",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "last",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "Ticker",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "NON_NULL"
                            },
                            "service": "matcher",
                            "name": "ticker",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "Ticker",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "matcher",
                            "name": "tickers",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "TradeConnection",
                                "kind": "OBJECT"
                            },
                            "service": "matcher",
                            "name": "trades",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "after",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "before",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "first",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Int",
                                        "kind": "SCALAR"
                                    },
                                    "name": "last",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "marketUuid",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": {
                                        "ofType": null,
                                        "name": "AssetPricesPayload",
                                        "kind": "OBJECT"
                                    },
                                    "name": null,
                                    "kind": "NON_NULL"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "service": "prezzo",
                            "name": "assetPrices",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": {
                                                "ofType": {
                                                    "name": "String",
                                                    "kind": "SCALAR"
                                                },
                                                "name": null,
                                                "kind": "NON_NULL"
                                            },
                                            "name": null,
                                            "kind": "LIST"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "baseAssets",
                                    "description": null,
                                    "defaultValue": null
                                },
                                {
                                    "type": {
                                        "ofType": {
                                            "ofType": null,
                                            "name": "String",
                                            "kind": "SCALAR"
                                        },
                                        "name": null,
                                        "kind": "NON_NULL"
                                    },
                                    "name": "quoteAsset",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Result",
                                "kind": "OBJECT"
                            },
                            "service": "ticket",
                            "name": "zendeskRedirectUrl",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "String",
                                        "kind": "SCALAR"
                                    },
                                    "name": "locale",
                                    "description": null,
                                    "defaultValue": null
                                }
                            ]
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "service": "ticket",
                    "possibleTypes": null,
                    "name": "Result",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "url",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "String",
                    "kind": "SCALAR",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": null,
                    "description": "The `String` scalar type represents textual data, represented as UTF-8character sequences. The String type is most often used by GraphQL trepresent free-form human-readable text."
                },
                {
                    "possibleTypes": null,
                    "name": "__Directive",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__DirectiveLocation",
                                    "kind": "ENUM"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "locations",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onField",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FIELD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onFragment",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value FRAGMENT_SPREAD",
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "onOperation",
                            "isDeprecated": true,
                            "description": null,
                            "deprecationReason": "Check `locations` field for enum value OPERATION",
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a directive"
                },
                {
                    "possibleTypes": null,
                    "name": "__DirectiveLocation",
                    "kind": "ENUM",
                    "interfaces": null,
                    "inputFields": null,
                    "fields": null,
                    "enumValues": [
                        {
                            "name": "FIELD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_DEFINITION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "FRAGMENT_SPREAD",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "INLINE_FRAGMENT",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "MUTATION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "QUERY",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        },
                        {
                            "name": "SUBSCRIPTION",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null
                        }
                    ],
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__EnumValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Field",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "args",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "deprecationReason",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "Boolean",
                                "kind": "SCALAR"
                            },
                            "name": "isDeprecated",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__InputValue",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "defaultValue",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "type",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": null
                },
                {
                    "possibleTypes": null,
                    "name": "__Schema",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Directive",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "directives",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "mutationType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "queryType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "subscriptionType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "types",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents a schema"
                },
                {
                    "possibleTypes": null,
                    "name": "__Type",
                    "kind": "OBJECT",
                    "interfaces": [],
                    "inputFields": null,
                    "fields": [
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "description",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__EnumValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "enumValues",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Field",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "fields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": [
                                {
                                    "type": {
                                        "ofType": null,
                                        "name": "Boolean",
                                        "kind": "SCALAR"
                                    },
                                    "name": "includeDeprecated",
                                    "description": null,
                                    "defaultValue": "false"
                                }
                            ]
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__InputValue",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "inputFields",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "interfaces",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "kind",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "String",
                                "kind": "SCALAR"
                            },
                            "name": "name",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": null,
                                "name": "__Type",
                                "kind": "OBJECT"
                            },
                            "name": "ofType",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        },
                        {
                            "type": {
                                "ofType": {
                                    "ofType": null,
                                    "name": "__Type",
                                    "kind": "OBJECT"
                                },
                                "name": null,
                                "kind": "LIST"
                            },
                            "name": "possibleTypes",
                            "isDeprecated": false,
                            "description": null,
                            "deprecationReason": null,
                            "args": []
                        }
                    ],
                    "enumValues": null,
                    "description": "Represents scalars, interfaces, object types, unions, enums in the system"
                }
            ],
            "subscriptionType": {
                "name": "RootSubscriptionType"
            },
            "queryType": {
                "name": "RootQueryType"
            },
            "mutationType": {
                "name": "RootMutationType"
            }
        }
    }
}
"""