from nose.tools import *
from ex49.sentence import *

def test_peek_returns_word_type():
  word = peek(word_list())
  assert_equal(word, 'stop')

def test_peek_returns_none_when_not_passed_word_list():
  word = peek(empty_word_list())
  assert_equal(word, None)

def test_match_returns_tuple_with_the_expecting_word_type():
  result = match(word_list(), 'stop')
  assert_equal(result, ('stop', 'of'))

def test_match_returns_none_with_the_expecting_word_type_does_not_match():
  result = match(word_list(), 'verb')
  assert_equal(result, None)

def test_match_returns_none_when_word_list_is_empty():
  result = match(empty_word_list(), 'verb')
  assert_equal(result, None)

def test_skip_returns_none_when_word_type_matches():
  result = skip(word_list(), 'stop')
  print result
  assert_equal(result, None)

def test_skip_returns_none_when_word_type_does_not_match():
  result = skip(word_list(), 'noun')
  assert_equal(result, None)

def test_parse_verb():
  result = parse_verb(verb_list())
  assert_equal(result, ('verb', 'go'))

@raises(ParseError)
def test_parse_verb_raises_error():
  parse_verb(word_list())

def test_parse_object_with_noun():
  noun_list = [('noun', 'princess')]
  result = parse_object(noun_list)
  assert_equal(result, ('noun', 'princess'))

def test_parse_object_with_direction():
  direction_list = [('direction', 'north')]
  result = parse_object(direction_list)
  assert_equal(result, ('direction', 'north'))

@raises(ParseError)
def test_parse_object_with_direction_raises_error():
  parse_object(empty_word_list())

def test_parse_subject():
  sentence_list = [('verb', 'go'), ('direction', 'north')]
  result = parse_subject(sentence_list, ('noun', 'cat'))
  assert_equal(result.subject, 'cat' )
  assert_equal(result.verb, 'go' )
  assert_equal(result.object, 'north' )

def test_parse_sentence():
  sentence_list = [('stop', 'of'), ('verb', 'go'), ('direction', 'north')]
  result = parse_sentence(sentence_list)
  assert_equal(result.subject, 'player')
  assert_equal(result.verb, 'go')
  assert_equal(result.object, 'north')

@raises(ParseError)
def test_parse_sentence_raises_error():
  parse_sentence(word_list())

#Givens

def word_list():
  return [('stop', 'of'), ('noun', 'princess'), ('verb', 'go')]

def empty_word_list():
  return []

def verb_list():
  return [('verb', 'go')]
