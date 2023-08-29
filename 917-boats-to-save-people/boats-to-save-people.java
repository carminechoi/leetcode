class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int left = 0;
        int right = people.length - 1;
        int count = 0;
        Arrays.sort(people);

        while(left <= right) {
            
            if(limit == people[left] + people[right]){
                count++;
                left++;
                right--;
            } else if(limit >= people[left] + people[right]) {
                count++;
                right--;
                left++;
            } else if(limit >= people[right]) {
                count++;
                right--;
            } else if(limit >= people[left]) {
                count++;
                left++;
            } 
        }
        return count;
    }
}