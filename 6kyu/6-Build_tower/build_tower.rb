def towerBuilder(n_floors)
  # tower = []
  # nbr_of_spaces = 0
  # space_caract = " "
  # dot_caract = "*"
  # impairs = (1..n_floors*2).step(2).first(n_floors)


  # impairs.each_with_index do |nbr_of_dots, index|
  #   floor = ""
  #   nbr_of_spaces = n_floors - index -1
  #   nbr_of_spaces.times {floor << space_caract}
  #   nbr_of_dots.times {floor << dot_caract}
  #   nbr_of_spaces.times {floor << space_caract}
  #   tower << floor

  (1..n_floors).map do |i|
    space = ' ' * (n_floors - i)
    stars = '*' * (i * 2 - 1)
    space + stars + space
  end

  # return tower
end

puts towerBuilder(5)
