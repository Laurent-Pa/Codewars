def longest(a1, a2)
 string = (a1+a2).chars.uniq.sort.join
end

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
expected = "abcdefklmopqwxy"
puts longest(a, b)
puts longest(a,b) == expected
