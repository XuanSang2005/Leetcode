function threeSum(nums: number[]): number[][] {
    const result: number[][] = [];
    // 1. Sắp xếp mảng (Bắt buộc để dùng Two Pointers và tránh trùng lặp)
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length - 2; i++) {
        // Bỏ qua số trùng lặp cho vị trí i
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            if (sum === 0) {
                // Thêm một mảng số [number, number, number] vào mảng 2 chiều
                result.push([nums[i], nums[left], nums[right]]);
                
                // Bỏ qua các số trùng lặp cho left và right
                while (left < right && nums[left] === nums[left + 1]) left++;
                while (left < right && nums[right] === nums[right - 1]) right--;
                
                left++;
                right--;
            } else if (sum < 0) {
                left++; // Tổng nhỏ quá thì tăng left để lấy số lớn hơn
            } else {
                right--; // Tổng lớn quá thì giảm right để lấy số nhỏ hơn
            }
        }
    }

    return result;
}