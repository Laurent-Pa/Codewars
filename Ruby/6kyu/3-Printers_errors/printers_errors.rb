def printer_error(string)
  # nbr_of_errors= string.chars.reject { |letter| letter <= 'm'}.length
  # error_rate = "#{nbr_of_errors}/#{string.length}"
  
  "#{string.count('n-z')}/#{string.length}"
end

s="aaabbbbhaijjjm"
puts printer_error(s)
