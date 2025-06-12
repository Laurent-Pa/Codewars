def find_outlier(integers)
  # déterminer si la série est paire ou impaire
  p first_is_even = integers[0].even?

  # déterminer si parmis les 2 premiers nombres, il y a l'intru
  if integers[1].even? != first_is_even
    return integers[2].even? == first_is_even ? integers[1] : integers [0]
  end

  # on rebalaye le tableau jusqu'à trouver l'intru
  integers.each do |number|
    return number if number.even? != first_is_even
  end
end

input = [2, 4, 0, 100, 4, 11, 2602, 36]
output = 11

puts find_outlier(input)

# Solution en une ligne
# integers.partition(&:odd?).find(&:one?).first
