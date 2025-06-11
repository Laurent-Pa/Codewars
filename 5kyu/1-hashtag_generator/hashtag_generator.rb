def generate_hashtag(str)
  words = str.split
  return false if words.length == 0

  hashtag = "##{words.map(&:capitalize).join}"
  if hashtag.length > 140
    return false
  end
  hashtag
end

str = " Hello there thanks for trying my Kata"
expected = "#HelloThereThanksForTryingMyKata"
puts generate_hashtag(str)
puts generate_hashtag(str) == expected
