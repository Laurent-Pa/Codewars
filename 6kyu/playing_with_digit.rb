# frozen_string_literal: true

def dig_pow(numb, par)
  # split the digits of n
  digits = numb.to_s.chars
  sum = 0
  digits.each_with_index do |digit, index|
    sum += digit.to_i**(index + par)
    puts sum
    puts rest = sum % n
    rest.zero ? sum / n : -1
  end
end

numb = 89
par = 1
dig_pow(numb, par)
