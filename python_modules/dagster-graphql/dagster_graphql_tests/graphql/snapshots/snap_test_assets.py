# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestAssetAwareEventLog.test_all_asset_keys[asset_aware_instance_in_process_env] 1'] = {
    'assetsOrError': {
        '__typename': 'AssetConnection',
        'nodes': [
            {
                'key': {
                    'path': [
                        'a'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'asset_one'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'asset_two'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'b'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'c'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'downstream_static_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'downstream_time_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'dummy_foreign_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'first_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'hanging_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'never_runs_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'upstream_static_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'upstream_time_partitioned_asset'
                    ]
                }
            }
        ]
    }
}

<<<<<<< HEAD
snapshots['TestAssetAwareEventLog.test_all_asset_keys[postgres_with_default_run_launcher_managed_grpc_env] 1'] = {
    'assetsOrError': {
        '__typename': 'AssetConnection',
        'nodes': [
            {
                'key': {
                    'path': [
                        'a'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'asset_one'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'asset_two'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'b'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'c'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'downstream_static_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'downstream_time_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'dummy_foreign_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'first_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'hanging_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'never_runs_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'upstream_static_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'upstream_time_partitioned_asset'
                    ]
                }
            }
        ]
    }
}

=======
>>>>>>> c1292165f1daf7b747ffae60013188b69171eae2
snapshots['TestAssetAwareEventLog.test_all_asset_keys[sqlite_with_default_run_launcher_managed_grpc_env] 1'] = {
    'assetsOrError': {
        '__typename': 'AssetConnection',
        'nodes': [
            {
                'key': {
                    'path': [
                        'a'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'asset_one'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'asset_two'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'b'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'c'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'downstream_static_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'downstream_time_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'dummy_foreign_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'first_asset'
                    ]
                }
<<<<<<< HEAD
            },
            {
                'key': {
                    'path': [
                        'hanging_asset'
                    ]
                }
            },
=======
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_asset_key_lineage[asset_aware_instance_in_process_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'assetLineage': [
                        {
                            'assetKey': {
                                'path': [
                                    'a'
                                ]
                            },
                            'partitions': [
                            ]
                        }
                    ],
                    'materialization': {
                        'label': 'b'
                    }
                }
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_asset_key_lineage[sqlite_with_default_run_launcher_managed_grpc_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'assetLineage': [
                        {
                            'assetKey': {
                                'path': [
                                    'a'
                                ]
                            },
                            'partitions': [
                            ]
                        }
                    ],
                    'materialization': {
                        'label': 'b'
                    }
                }
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_asset_key_materialization[asset_aware_instance_in_process_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
>>>>>>> c1292165f1daf7b747ffae60013188b69171eae2
            {
                'key': {
                    'path': [
                        'never_runs_asset'
                    ]
                }
<<<<<<< HEAD
            },
            {
                'key': {
                    'path': [
                        'upstream_static_partitioned_asset'
                    ]
                }
            },
            {
                'key': {
                    'path': [
                        'upstream_time_partitioned_asset'
                    ]
                }
            }
=======
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_asset_key_materialization[sqlite_with_default_run_launcher_managed_grpc_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'assetLineage': [
                    ],
                    'materialization': {
                        'label': 'a'
                    }
                }
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_asset_key_not_found[asset_aware_instance_in_process_env] 1'] = {
    'assetOrError': {
        '__typename': 'AssetNotFoundError'
    }
}

snapshots['TestAssetAwareEventLog.test_get_asset_key_not_found[sqlite_with_default_run_launcher_managed_grpc_env] 1'] = {
    'assetOrError': {
        '__typename': 'AssetNotFoundError'
    }
}

snapshots['TestAssetAwareEventLog.test_get_partitioned_asset_key_lineage[asset_aware_instance_in_process_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'assetLineage': [
                        {
                            'assetKey': {
                                'path': [
                                    'a'
                                ]
                            },
                            'partitions': [
                                '1'
                            ]
                        }
                    ],
                    'materialization': {
                        'label': 'b'
                    }
                }
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_partitioned_asset_key_lineage[sqlite_with_default_run_launcher_managed_grpc_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'assetLineage': [
                        {
                            'assetKey': {
                                'path': [
                                    'a'
                                ]
                            },
                            'partitions': [
                                '1'
                            ]
                        }
                    ],
                    'materialization': {
                        'label': 'b'
                    }
                }
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_partitioned_asset_key_materialization[asset_aware_instance_in_process_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'materialization': {
                        'label': 'a'
                    }
                },
                'partition': 'partition_1'
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_partitioned_asset_key_materialization[sqlite_with_default_run_launcher_managed_grpc_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'materialization': {
                        'label': 'a'
                    }
                },
                'partition': 'partition_1'
            }
>>>>>>> c1292165f1daf7b747ffae60013188b69171eae2
        ]
    }
}
