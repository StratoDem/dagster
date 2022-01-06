Snowflake (dagster-snowflake)
-----------------------------

This library provides an integration with the `Snowflake <https://www.snowflake.com/>`_ data
warehouse.

It provides a ``snowflake_resource``, which is a Dagster resource for configuring
Snowflake connections and issuing queries, as well as a ``snowflake_op_for_query`` function for
constructing ops that execute Snowflake queries.

To use this library, you should first ensure that you have an appropriate `Snowflake user
<https://docs.snowflake.net/manuals/user-guide/admin-user-management.html>`_ configured to access
your data warehouse.


.. currentmodule:: dagster_snowflake

.. autoconfigurable:: snowflake_resource
  :annotation: ResourceDefinition

.. autofunction:: snowflake_op_for_query

.. autoclass:: SnowflakeConnection
  :members:
  :undoc-members:
