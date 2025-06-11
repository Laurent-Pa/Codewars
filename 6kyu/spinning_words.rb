def spin_words(string)
string.split.map { |s| s.length >= 5 ? s.reverse : s }.join ' '
end

testing_words = "Welcome"
result = "emocleW"
if spin_words(testing_words) == result
  puts "test completed"
else
  puts "test has failed"
end
