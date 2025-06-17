def first_non_repeating_letter(s)
  # My solution
  all_uniq = ""
  string_repartition = s.downcase.chars.tally

  s.chars.each_with_index do |letter, index|
   all_uniq << s[index] if string_repartition[letter.downcase] == 1
  end
  p all_uniq.empty? ? "" : all_uniq[0]

  # Single line solution
  s.chars.find {|i| s.downcase.count(i)==1 || s.upcase.count(i)==1} || ""
end

puts  first_non_repeating_letter("STress") == "T"
