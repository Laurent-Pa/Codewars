def count_bits(n)
  n.to_s(2).count("1")
end

puts count_bits(0)
