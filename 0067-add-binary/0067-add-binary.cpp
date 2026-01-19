class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.size() - 1; //1
        int j = b.size() - 1; //0
        int carry = 0;
        string result;
        while (i >= 0 || j >= 0){
            int sum = carry; //0 1
            if (i >= 0){
                sum += a[i] - '0'; //sum = 1 sum = 2
                i--;
            }
            if (j >= 0){
                sum += b[j] - '0'; //sum = 2
                j--;
            }
            carry = sum / 2; //1
            sum = sum % 2; //sum = 0
            result += to_string(sum);
            sum = 0;
            cout<< result << " ";
        }
        if (carry != 0) result += to_string(carry);
        reverse(result.begin(), result.end());
        return result;   
    }
};