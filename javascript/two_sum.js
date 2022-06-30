// 1. 투썸
// 정수 배열이 주어지면 두 숫자의 인덱스를 반환하여 특정 대상에 합산되도록 합니다.

// 각 입력에 정확히 하나의 솔루션이 있다고 가정할 수 있습니다.

// 예: 주어진 숫자 = [2, 7, 11, 15], 대상 = 9,

// nums[0] + nums[1] = 2 + 7 = 9이므로 [0, 1]을 반환합니다.

//이중 반복문
var twoSum = function(nums, target) {
    for(let i = 0; i < nums.length; ++i) {
        for(let j = i + 1; j < nums.length; ++j) {
          if(nums[i] + nums[j] === target) return [i, j];
        }
      }
};


//해쉬 테이블 이용
var twoSum = function(nums, target) {
    let hash = {};
    for(let i in nums) {
      if(hash[target - nums[i]]) return [i, hash[target - nums[i]]];
      hash[nums[i]] = i;
    }
};


console.log(twoSum([1,2,3,4],7))