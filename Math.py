class Math:
    """
    Minimal class that performs 1D convolution (valid mode).
    Pure Python implementation.
    """

    def convolve(self, signal, kernel):
        """
        Perform 1D convolution between 'signal' and 'kernel'.
        - Both inputs should be lists of numbers.
        - Uses valid convolution (no padding).
        """
        n = len(signal)
        k = len(kernel)

        if k > n:
            raise ValueError("Kernel length must be <= signal length.")

        # Flip kernel for convolution operation
        kernel_flipped = kernel[::-1]

        result = []
        for i in range(n - k + 1):
            window = signal[i:i+k]
            value = sum(window[j] * kernel_flipped[j] for j in range(k))
            result.append(value)

        return result
