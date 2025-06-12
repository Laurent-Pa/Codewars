def alphabet_position(text)
position = []
text.gsub(/[^a-zA-Z]/, '').chars.each {|letter| position << letter.downcase.ord - 96}
puts position.join(" ")
end

# Tests examples

input = "The sunset sets at twelve o' clock."
output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

puts alphabet_position(input) == output
