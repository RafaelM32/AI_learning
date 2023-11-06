input = [1, 2, 3, 2.5]
weights_1 = [0.2, 0.8, -0.5, 1.0]
weights_2 = [0.5, -0.91, 0.26, -0.5]
weights_3 = [-0.26, -0.27, 0.17, 0.87]
bias_1 = 2
bias_2 = 3
bias_3 = 0.5

output = [input[0]*weights_1[0] + input[1]*weights_1[1] + input[2]*weights_1[2] + input[3]*weights_1[3] + bias_1,
          input[0]*weights_2[0] + input[1]*weights_2[1] + input[2]*weights_2[2] + input[3]*weights_2[3] + bias_2,
          input[0]*weights_3[0] + input[1]*weights_3[1] + input[2]*weights_3[2] + input[3]*weights_3[3] + bias_3]

print(output)