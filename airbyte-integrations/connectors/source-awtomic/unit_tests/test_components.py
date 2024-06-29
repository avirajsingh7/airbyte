#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from unittest.mock import Mock, patch
from source_awtomic.components import LastEvaluatedKeyPaginationStrategy


def test_next_page_token_with_last_evaluated_key(self):

    response = Mock()
    response.json.return_value = {'LastEvaluatedKey': {'key1': 'value1', 'key2': 'value2'}}
    pagination_strategy = LastEvaluatedKeyPaginationStrategy()
    next_page_token = pagination_strategy.next_page_token(response, [])
    self.assertIsNotNone(next_page_token)
    self.assertEqual(next_page_token, '{"key1": "value1", "key2": "value2"}')

def test_next_page_token_without_last_evaluated_key(self):

    response = Mock()
    response.json.return_value = {}
    pagination_strategy = LastEvaluatedKeyPaginationStrategy()
    next_page_token = pagination_strategy.next_page_token(response, [])
    self.assertIsNone(next_page_token)
